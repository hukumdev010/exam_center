"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { CategorySelector } from "@/components/CategorySelector";

export default function Home() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const handleCertificationSelect = async (slug: string, name: string) => {
    setLoading(true);
    
    // Navigate to the quiz page
    router.push(`/quiz/${slug}`);
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

  return <CategorySelector onCertificationSelect={handleCertificationSelect} />;
}
