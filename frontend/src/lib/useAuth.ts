import { useState, useEffect } from 'react'
import { authService, AuthState } from './auth'

export function useAuth() {
  const [authState, setAuthState] = useState<AuthState>(authService.getState())

  useEffect(() => {
    const unsubscribe = authService.subscribe(setAuthState)
    return unsubscribe
  }, [])

  return {
    user: authState.user,
    isAuthenticated: authState.isAuthenticated,
    isLoading: authState.isLoading,
    signIn: () => authService.signInWithGoogle(),
    signOut: () => authService.signOut(),
    handleAuthCallback: (code: string) => authService.handleAuthCallback(code)
  }
}

// For backward compatibility with existing code
export function useSession() {
  const auth = useAuth()
  
  return {
    data: auth.isAuthenticated ? { user: auth.user } : null,
    status: auth.isLoading ? 'loading' : auth.isAuthenticated ? 'authenticated' : 'unauthenticated'
  }
}
