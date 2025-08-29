"use client";

import { useState } from "react";
import { ExamQuiz } from "@/components/ExamQuiz";
import { CategorySelector } from "@/components/CategorySelector";
import { Button } from "@/components/ui/button";
import { ArrowLeft } from "lucide-react";

type Question = {
  id: number;
  text: string;
  explanation?: string;
  points: number;
  answers: Answer[];
};

type Answer = {
  id: number;
  text: string;
  isCorrect: boolean;
};

type Certification = {
  id: number;
  name: string;
  description: string;
  slug: string;
  level: string;
  duration: number;
  questionsCount: number;
  questions: Question[];
};

export default function Home() {
  const [selectedCertification, setSelectedCertification] = useState<{
    slug: string;
    name: string;
  } | null>(null);
  const [certificationData, setCertificationData] = useState<Certification | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleCertificationSelect = async (slug: string, name: string) => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`/api/certifications/${slug}`);
      if (!response.ok) {
        throw new Error('Failed to fetch certification data');
      }
      const data = await response.json();

      setSelectedCertification({ slug, name });
      setCertificationData(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleBackToSelection = () => {
    setSelectedCertification(null);
    setCertificationData(null);
    setError(null);
  };

  if (!selectedCertification) {
    return <CategorySelector onCertificationSelect={handleCertificationSelect} />;
  }

  if (loading) {
    return (
      <main className="min-h-screen bg-slate-50 py-8">
        <div className="max-w-2xl mx-auto p-6">
          <div className="text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
            <p className="mt-2 text-slate-600">Loading {selectedCertification.name}...</p>
          </div>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="min-h-screen bg-slate-50 py-8">
        <div className="max-w-2xl mx-auto p-6">
          <div className="mb-6">
            <Button
              variant="outline"
              onClick={handleBackToSelection}
              className="inline-flex items-center gap-2"
            >
              <ArrowLeft className="w-4 h-4" />
              Back to Categories
            </Button>
          </div>
          <div className="text-center">
            <p className="text-red-600 mb-4">Error: {error}</p>
            <Button onClick={() => handleCertificationSelect(selectedCertification.slug, selectedCertification.name)}>
              Try Again
            </Button>
          </div>
        </div>
      </main>
    );
  }

  if (!certificationData) {
    return (
      <main className="min-h-screen bg-slate-50 py-8">
        <div className="max-w-2xl mx-auto p-6">
          <div className="mb-6">
            <Button
              variant="outline"
              onClick={handleBackToSelection}
              className="inline-flex items-center gap-2"
            >
              <ArrowLeft className="w-4 h-4" />
              Back to Categories
            </Button>
          </div>
          <div className="text-center">
            <p className="text-slate-600">No questions found for this certification.</p>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-slate-50 py-8">
      <div className="max-w-2xl mx-auto p-6">
        <div className="mb-6">
          <Button
            variant="outline"
            onClick={handleBackToSelection}
            className="inline-flex items-center gap-2"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Categories
          </Button>
        </div>
        <ExamQuiz
          key={selectedCertification.slug}
          questions={certificationData.questions}
          certificationName={certificationData.name}
        />
      </div>
    </main>
  );
}
