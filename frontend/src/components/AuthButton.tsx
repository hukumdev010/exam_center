"use client"

import { Button } from "@/components/ui/button"
import { LogOut } from "lucide-react"
import { useAuth } from "@/lib/useAuth"

export function AuthButton() {
    const { user, isAuthenticated, isLoading, signIn, signOut } = useAuth()

    if (isLoading) {
        return <div className="h-10 w-20 bg-gray-200 animate-pulse rounded"></div>
    }

    if (isAuthenticated) {
        return (
            <div className="flex items-center gap-3">
                <div className="flex items-center gap-2">
                    <span className="font-medium text-gray-900">
                        {user?.name}
                    </span>
                </div>
                <Button
                    onClick={() => signOut()}
                    variant="outline"
                    size="sm"
                    className="flex items-center gap-2"
                >
                    <LogOut className="w-4 h-4" />
                    Sign out
                </Button>
            </div>
        )
    }

    return (
        <Button
            onClick={() => signIn()}
            className="bg-blue-600 hover:bg-blue-700"
        >
            Sign in with Google
        </Button>
    )
}
