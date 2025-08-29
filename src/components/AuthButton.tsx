"use client"

import { signIn, signOut, useSession } from "next-auth/react"
import { Button } from "@/components/ui/button"
import { LogOut } from "lucide-react"


export function AuthButton() {
    const { data: session, status } = useSession()

    if (status === "loading") {
        return <div className="h-10 w-20 bg-gray-200 animate-pulse rounded"></div>
    }

    if (session) {
        return (
            <div className="flex items-center gap-3">
                <div className="flex items-center gap-2">
                    <span className="font-medium text-gray-900">
                        {session.user?.name}
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
            onClick={() => signIn("google")}
            className="bg-blue-600 hover:bg-blue-700"
        >
            Sign in with Google
        </Button>
    )
}
