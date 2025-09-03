"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "@/lib/useAuth";
import { QuestionCard } from "./QuestionCard";
import { Progress } from "./ui/progress";
import { Button } from "./ui/button";
import { RotateCcw, Trophy } from "lucide-react";
import { API_ENDPOINTS } from "@/lib/api-config";

type Answer = {
    id: number;
    text: string;
    isCorrect: boolean;
};

type Question = {
    id: number;
    text: string;
    explanation?: string;
    points: number;
    answers: Answer[];
};

interface ExamQuizProps {
    questions: Question[];
    certificationName: string;
    certificationSlug?: string;
    certificationId?: number;
    initialQuestion?: number;
}

export function ExamQuiz({ questions, certificationName, certificationSlug, certificationId, initialQuestion = 0 }: ExamQuizProps) {
    const router = useRouter();
    const { data: session } = useSession();
    const [currentQuestion, setCurrentQuestion] = useState(initialQuestion);
    const [score, setScore] = useState(0);
    const [sessionScore, setSessionScore] = useState(0); // Live session score
    const [answeredQuestions, setAnsweredQuestions] = useState<Set<number>>(new Set());
    const [isCompleted, setIsCompleted] = useState(false);
    const [totalPoints, setTotalPoints] = useState(0);
    const [canProceed, setCanProceed] = useState(false);

    // Initialize state from localStorage if available, or from user progress if logged in
    useEffect(() => {
        const fetchUserProgress = async () => {
            try {
                // For now, we'll use a mock token. In production, implement proper JWT handling
                const token = localStorage.getItem('auth_token') || 'mock_token';
                const response = await fetch(API_ENDPOINTS.progress, {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                if (response.ok) {
                    const progressData = await response.json();
                    const currentProgress = progressData.find((p: { certificationId: number }) => p.certificationId === certificationId);

                    if (currentProgress) {
                        setCurrentQuestion(currentProgress.currentQuestion);
                        setScore(currentProgress.correctAnswers);
                        setTotalPoints(currentProgress.points);
                        setIsCompleted(currentProgress.isCompleted);

                        // Reconstruct answered questions based on current question
                        const answered = new Set<number>();
                        for (let i = 0; i < currentProgress.currentQuestion; i++) {
                            answered.add(i);
                        }
                        setAnsweredQuestions(answered);
                    }
                }
            } catch (error) {
                console.error('Failed to fetch user progress:', error);
            }
        };

        // Reset session score when component mounts
        setSessionScore(0);
        setCanProceed(false);

        if (session?.user?.id && certificationId) {
            // Fetch user progress from API
            // fetchUserProgress();
        } else if (certificationSlug) {
            // Fallback to localStorage for non-authenticated users
            const savedState = localStorage.getItem(`quiz-${certificationSlug}`);
            if (savedState) {
                const state = JSON.parse(savedState);
                setScore(state.score || 0);
                setAnsweredQuestions(new Set(state.answeredQuestions || []));
                setIsCompleted(state.isCompleted || false);
                setTotalPoints(state.totalPoints || 0);
            }
        }
    }, [certificationSlug, certificationId, session?.user?.id]);

    // Reset state when question changes
    useEffect(() => {
        setCanProceed(false);
    }, [currentQuestion]);

    const saveQuizAttempt = async () => {
        if (!session?.user?.id || !certificationId) return;

        try {
            const token = localStorage.getItem('auth_token') || 'mock_token';
            await fetch(API_ENDPOINTS.quizAttempts, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    certificationId,
                    score: Math.round((score / questions.length) * 100),
                    totalQuestions: questions.length,
                    correctAnswers: score,
                    points: totalPoints
                })
            });
        } catch (error) {
            console.error('Failed to save quiz attempt:', error);
        }
    };

    // Update URL when question changes
    const updateURL = (questionIndex: number) => {
        if (certificationSlug) {
            router.replace(`/quiz/${certificationSlug}?q=${questionIndex}`, { scroll: false });
        }
    };

    // Save state to localStorage for non-authenticated users
    const saveLocalState = (newScore: number, newAnsweredQuestions: Set<number>, newIsCompleted: boolean, newTotalPoints: number) => {
        if (certificationSlug && !session?.user?.id) {
            localStorage.setItem(`quiz-${certificationSlug}`, JSON.stringify({
                score: newScore,
                answeredQuestions: Array.from(newAnsweredQuestions),
                isCompleted: newIsCompleted,
                totalPoints: newTotalPoints
            }));
        }
    };

    // Save progress to API for authenticated users
    const saveProgress = async (questionIndex: number, correctAnswers: number, points: number, completed: boolean) => {
        if (session?.user?.id && certificationId) {
            try {
                const token = localStorage.getItem('auth_token') || 'mock_token';
                await fetch(API_ENDPOINTS.progress, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        certificationId,
                        currentQuestion: questionIndex,
                        correctAnswers,
                        points,
                        isCompleted: completed
                    })
                });
            } catch (error) {
                console.error('Failed to save user progress:', error);
            }
        }
    };

    const progress = ((currentQuestion + 1) / questions.length) * 100;
    const correctAnswers = score;
    const totalQuestions = questions.length;

    const handleAnswer = (isCorrect: boolean, points: number) => {
        if (answeredQuestions.has(currentQuestion)) return;

        const newAnsweredQuestions = new Set(answeredQuestions).add(currentQuestion);
        const newScore = isCorrect ? score + 1 : score;
        const newTotalPoints = isCorrect ? totalPoints + points : totalPoints;

        // Update session score (live scoring)
        if (isCorrect) {
            setSessionScore(prev => prev + 1);
        }

        setAnsweredQuestions(newAnsweredQuestions);
        setScore(newScore);
        setTotalPoints(newTotalPoints);

        // Save state
        saveLocalState(newScore, newAnsweredQuestions, isCompleted, newTotalPoints);
        saveProgress(currentQuestion, newScore, newTotalPoints, isCompleted);
    };

    const handleSubmit = (isCorrect: boolean, canProceed: boolean) => {
        setCanProceed(canProceed);
    };

    const handleNext = () => {
        if (!canProceed) return; // Only proceed if current question is correct

        if (currentQuestion < questions.length - 1) {
            const nextQuestion = currentQuestion + 1;
            setCurrentQuestion(nextQuestion);
            setCanProceed(false); // Reset for next question
            updateURL(nextQuestion);
            saveProgress(nextQuestion, score, totalPoints, false);
        } else {
            const newIsCompleted = true;
            setIsCompleted(newIsCompleted);
            saveLocalState(score, answeredQuestions, newIsCompleted, totalPoints);
            saveProgress(currentQuestion, score, totalPoints, newIsCompleted);
            saveQuizAttempt();
        }
    };

    const handlePrevious = () => {
        if (currentQuestion > 0) {
            const prevQuestion = currentQuestion - 1;
            setCurrentQuestion(prevQuestion);
            updateURL(prevQuestion);
            saveProgress(prevQuestion, score, totalPoints, false);
        }
    };

    const handleRestart = () => {
        setCurrentQuestion(0);
        setScore(0);
        setSessionScore(0); // Reset session score
        setTotalPoints(0);
        setAnsweredQuestions(new Set());
        setIsCompleted(false);
        setCanProceed(false);

        // Clear saved state
        if (certificationSlug && !session?.user?.id) {
            localStorage.removeItem(`quiz-${certificationSlug}`);
        }

        // Update URL to first question
        updateURL(0);

        // Reset progress in database
        saveProgress(0, 0, 0, false);
    };

    const getScoreColor = () => {
        const percentage = (correctAnswers / totalQuestions) * 100;
        if (percentage >= 80) return "text-green-600";
        if (percentage >= 60) return "text-yellow-600";
        return "text-red-600";
    };

    const handleBackHome = () => {
        router.push('/');
    };

    if (isCompleted) {
        return (
            <div className="max-w-2xl mx-auto p-6">
                <div className="bg-white rounded-lg border border-slate-200 p-8 shadow-sm text-center">
                    <Trophy className="w-16 h-16 mx-auto mb-4 text-yellow-500" />
                    <h2 className="text-2xl font-bold text-slate-900 mb-2">Quiz Completed!</h2>
                    <p className="text-slate-600 mb-6">{certificationName}</p>

                    <div className="bg-slate-50 rounded-lg p-6 mb-6">
                        <div className="text-3xl font-bold mb-2">
                            <span className={getScoreColor()}>
                                {correctAnswers}/{totalQuestions}
                            </span>
                        </div>
                        <p className="text-slate-600 mb-2">
                            You scored {Math.round((correctAnswers / totalQuestions) * 100)}%
                        </p>
                        <p className="text-sm text-slate-500">
                            Total Points: {totalPoints}
                        </p>
                    </div>

                    <div className="flex gap-4 justify-center">
                        <Button onClick={handleRestart} variant="outline" className="inline-flex items-center gap-2">
                            <RotateCcw className="w-4 h-4" />
                            Restart Quiz
                        </Button>
                        <Button onClick={handleBackHome} className="bg-blue-600 hover:bg-blue-700">
                            Back to Home
                        </Button>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="max-w-2xl mx-auto p-6">
            <div className="mb-6">
                <div className="flex items-center justify-between mb-2">
                    <h1 className="text-2xl font-bold text-slate-900">{certificationName}</h1>
                    <div className="text-sm text-slate-600">
                        Question {currentQuestion + 1} of {questions.length}
                    </div>
                </div>
                <Progress value={progress} className="w-full" />

                {/* Live Session Stats */}
                <div className="mt-2 text-center">
                    <span className="text-sm text-green-600 font-medium">
                        Session Correct: {sessionScore}
                    </span>
                    <span className="text-sm text-slate-500 mx-2">|</span>
                    <span className="text-sm text-slate-600">
                        Total Points: {totalPoints}
                    </span>
                </div>
            </div>

            <div className="mb-6">
                <QuestionCard
                    question={questions[currentQuestion]}
                    onAnswer={handleAnswer}
                    onSubmit={handleSubmit}
                />
            </div>

            <div className="flex items-center justify-between">
                <Button
                    variant="outline"
                    onClick={handlePrevious}
                    disabled={currentQuestion === 0}
                >
                    Previous
                </Button>

                <div className="text-sm text-slate-600 text-center">
                    <span className="font-medium">
                        {canProceed ? "Ready to proceed!" : "Submit your answer to continue"}
                    </span>
                </div>

                {canProceed ? (
                    <Button onClick={handleNext} className="bg-green-600 hover:bg-green-700">
                        {currentQuestion === questions.length - 1 ? "Finish" : "Next"}
                    </Button>
                ) : (
                    <Button disabled className="bg-slate-300">
                        {currentQuestion === questions.length - 1 ? "Finish" : "Next"}
                    </Button>
                )}
            </div>
        </div>
    );
}
