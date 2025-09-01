"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { CategorySelector } from "@/components/CategorySelector";
import { ProgressDashboard } from "@/components/ProgressDashboard";
import { AuthButton } from "@/components/AuthButton";
import { Button } from "@/components/ui/button";
import { User } from "lucide-react";
import Link from "next/link";

export default function Home() {
  const router = useRouter();
  const { data: session, status } = useSession();
  const [loading, setLoading] = useState(false);
  const [showCategorySelector, setShowCategorySelector] = useState(false);

  const handleCertificationSelect = async (slug: string) => {
    setLoading(true);
    router.push(`/quiz/${slug}`);
  };

  const handleContinueQuiz = (slug: string) => {
    setLoading(true);
    router.push(`/quiz/${slug}`);
  };

  const handleStartNewQuiz = () => {
    setShowCategorySelector(true);
  };

  if (loading) {
    return (
      <main className="min-h-screen bg-slate-50 py-8">
        <div className="max-w-2xl mx-auto p-6">
          <div className="text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
            <p className="mt-2 text-slate-600">Loading...</p>
          </div>
        </div>
      </main>
    );
  }

  if (status === "loading") {
    return (
      <main className="min-h-screen bg-slate-50 py-8">
        <div className="max-w-6xl mx-auto p-6">
          <div className="animate-pulse">
            <div className="h-8 bg-gray-200 rounded w-1/4 mb-6"></div>
            <div className="space-y-4">
              {[1, 2, 3].map((i) => (
                <div key={i} className="h-24 bg-gray-200 rounded-lg" />
              ))}
            </div>
          </div>
        </div>
      </main>
    );
  }

  if (showCategorySelector || !session) {
    return (
      <main className="min-h-screen bg-slate-50">
        <div className="bg-white border-b border-gray-200">
          <div className="max-w-6xl mx-auto px-6 py-4">
            <div className="flex justify-between items-center">
              <div className="flex items-center gap-4">
                <h1 className="text-xl font-bold text-gray-900">Exam Center</h1>
                {showCategorySelector && (
                  <Button
                    onClick={() => setShowCategorySelector(false)}
                    variant="outline"
                    size="sm"
                  >
                    ← Back to Dashboard
                  </Button>
                )}
              </div>
              <div className="flex items-center gap-4">
                {session && (
                  <Link href="/profile">
                    <Button variant="outline" size="sm" className="flex items-center gap-2">
                      <User className="w-4 h-4" />
                      Profile
                    </Button>
                  </Link>
                )}
                <AuthButton />
              </div>
            </div>
          </div>
        </div>

        <div className="py-8">
          <CategorySelector onCertificationSelect={handleCertificationSelect} />
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-slate-50">
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold text-gray-900">Welcome back, {session.user?.name?.split(' ')[0]}!</h1>
            <div className="flex items-center gap-4">
              <Link href="/profile">
                <Button variant="outline" size="sm" className="flex items-center gap-2">
                  <User className="w-4 h-4" />
                  Profile
                </Button>
              </Link>
              <AuthButton />
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-6xl mx-auto p-6">
        <ProgressDashboard
          onContinueQuiz={handleContinueQuiz}
          onStartNewQuiz={handleStartNewQuiz}
        />
      </div>
    </main>
  );
}
