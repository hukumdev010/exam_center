"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { QuestionCard } from "./QuestionCard";
import { Progress } from "./ui/progress";
import { Button } from "./ui/button";
import { RotateCcw, Trophy } from "lucide-react";

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
    initialQuestion?: number;
}

export function ExamQuiz({ questions, certificationName, certificationSlug, initialQuestion = 0 }: ExamQuizProps) {
    const router = useRouter();
    const [currentQuestion, setCurrentQuestion] = useState(initialQuestion);
    const [score, setScore] = useState(0);
    const [answeredQuestions, setAnsweredQuestions] = useState<Set<number>>(new Set());
    const [isCompleted, setIsCompleted] = useState(false);

    // Initialize state from localStorage if available
    useEffect(() => {
        if (certificationSlug) {
            const savedState = localStorage.getItem(`quiz-${certificationSlug}`);
            if (savedState) {
                const state = JSON.parse(savedState);
                setScore(state.score || 0);
                setAnsweredQuestions(new Set(state.answeredQuestions || []));
                setIsCompleted(state.isCompleted || false);
            }
        }
    }, [certificationSlug]);

    // Update URL when question changes
    const updateURL = (questionIndex: number) => {
        if (certificationSlug) {
            router.replace(`/quiz/${certificationSlug}?q=${questionIndex}`, { scroll: false });
        }
    };

    // Save state to localStorage
    const saveState = (newScore: number, newAnsweredQuestions: Set<number>, newIsCompleted: boolean) => {
        if (certificationSlug) {
            localStorage.setItem(`quiz-${certificationSlug}`, JSON.stringify({
                score: newScore,
                answeredQuestions: Array.from(newAnsweredQuestions),
                isCompleted: newIsCompleted
            }));
        }
    };

    const progress = ((currentQuestion + 1) / questions.length) * 100;
    const correctAnswers = score;
    const totalQuestions = questions.length;

    const handleAnswer = (isCorrect: boolean, points: number) => {
        if (answeredQuestions.has(currentQuestion)) return;

        const newAnsweredQuestions = new Set(answeredQuestions).add(currentQuestion);
        const newScore = isCorrect ? score + points : score;
        
        setAnsweredQuestions(newAnsweredQuestions);
        setScore(newScore);
        
        // Save state
        saveState(newScore, newAnsweredQuestions, isCompleted);
    };

    const handleNext = () => {
        if (currentQuestion < questions.length - 1) {
            const nextQuestion = currentQuestion + 1;
            setCurrentQuestion(nextQuestion);
            updateURL(nextQuestion);
        } else {
            const newIsCompleted = true;
            setIsCompleted(newIsCompleted);
            saveState(score, answeredQuestions, newIsCompleted);
        }
    };

    const handlePrevious = () => {
        if (currentQuestion > 0) {
            const prevQuestion = currentQuestion - 1;
            setCurrentQuestion(prevQuestion);
            updateURL(prevQuestion);
        }
    };

    const handleRestart = () => {
        setCurrentQuestion(0);
        setScore(0);
        setAnsweredQuestions(new Set());
        setIsCompleted(false);
        
        // Clear saved state
        if (certificationSlug) {
            localStorage.removeItem(`quiz-${certificationSlug}`);
        }
        
        // Update URL to first question
        updateURL(0);
    };

    const getScoreColor = () => {
        const percentage = (correctAnswers / totalQuestions) * 100;
        if (percentage >= 80) return "text-green-600";
        if (percentage >= 60) return "text-yellow-600";
        return "text-red-600";
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
                        <p className="text-slate-600">
                            You scored {Math.round((correctAnswers / totalQuestions) * 100)}%
                        </p>
                    </div>

                    <Button onClick={handleRestart} className="inline-flex items-center gap-2">
                        <RotateCcw className="w-4 h-4" />
                        Restart Quiz
                    </Button>
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
            </div>

            <div className="mb-6">
                <QuestionCard
                    question={questions[currentQuestion]}
                    onAnswer={handleAnswer}
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

                <div className="text-sm text-slate-600">
                    Score: <span className="font-medium">{score}/{answeredQuestions.size}</span>
                </div>

                <Button
                    onClick={handleNext}
                    disabled={!answeredQuestions.has(currentQuestion)}
                >
                    {currentQuestion === questions.length - 1 ? "Finish" : "Next"}
                </Button>
            </div>
        </div>
    );
}
