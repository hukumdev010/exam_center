"use client";

import { useState } from "react";
import { cn } from "@/lib/utils";
import { CheckCircle2, XCircle, Info } from "lucide-react";

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

interface QuestionCardProps {
    question: Question;
    onAnswer: (isCorrect: boolean, points: number) => void;
}

export function QuestionCard({ question, onAnswer }: QuestionCardProps) {
    const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
    const [showExplanation, setShowExplanation] = useState(false);
    const [hasAnswered, setHasAnswered] = useState(false);
    const [earnedPoints, setEarnedPoints] = useState(0);

    const handleAnswerSelect = (answer: Answer) => {
        if (hasAnswered) return;

        setSelectedAnswer(answer.id);
        setHasAnswered(true);

        const points = answer.isCorrect ? question.points : 0;
        setEarnedPoints(points);
        onAnswer(answer.isCorrect, points);
    };

    const getAnswerStyle = (answer: Answer) => {
        if (!hasAnswered) {
            return "hover:bg-slate-50 border-slate-200";
        }

        if (selectedAnswer === answer.id) {
            return answer.isCorrect
                ? "bg-green-50 border-green-300 text-green-800"
                : "bg-red-50 border-red-300 text-red-800";
        }

        if (answer.isCorrect) {
            return "bg-green-50 border-green-300 text-green-800";
        }

        return "bg-slate-50 border-slate-200 text-slate-500";
    };

    const getAnswerIcon = (answer: Answer) => {
        if (!hasAnswered) return null;

        if (answer.isCorrect) {
            return <CheckCircle2 className="w-5 h-5 text-green-600" />;
        }

        if (selectedAnswer === answer.id && !answer.isCorrect) {
            return <XCircle className="w-5 h-5 text-red-600" />;
        }

        return null;
    };

    return (
        <div className="bg-white rounded-lg border border-slate-200 p-6 shadow-sm">
            <div className="mb-6">
                <h3 className="text-lg font-medium text-slate-900 leading-relaxed">
                    {question.text}
                </h3>
            </div>

            <div className="space-y-3 mb-6">
                {question.answers.map((answer) => (
                    <button
                        key={answer.id}
                        className={cn(
                            "w-full p-4 text-left rounded-lg border-2 transition-all duration-200 flex items-center justify-between group",
                            getAnswerStyle(answer),
                            !hasAnswered && "hover:border-slate-300"
                        )}
                        onClick={() => handleAnswerSelect(answer)}
                        disabled={hasAnswered}
                    >
                        <span className="text-sm font-medium">{answer.text}</span>
                        {getAnswerIcon(answer)}
                    </button>
                ))}
            </div>

            <div className="flex items-center justify-between pt-4 border-t border-slate-200">
                <button
                    className="inline-flex items-center gap-2 text-sm text-slate-600 hover:text-slate-900 transition-colors"
                    onClick={() => setShowExplanation(!showExplanation)}
                >
                    <Info className="w-4 h-4" />
                    {showExplanation ? "Hide" : "Show"} Explanation
                </button>

                {hasAnswered && (
                    <div className="text-sm font-medium">
                        {earnedPoints > 0 ? (
                            <span className="text-green-600">+{earnedPoints} point{earnedPoints > 1 ? 's' : ''}</span>
                        ) : (
                            <span className="text-slate-500">0 points</span>
                        )}
                    </div>
                )}
            </div>

            {showExplanation && question.explanation && (
                <div className="mt-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                    <p className="text-sm text-blue-800 leading-relaxed">
                        {question.explanation}
                    </p>
                </div>
            )}
        </div>
    );
}
