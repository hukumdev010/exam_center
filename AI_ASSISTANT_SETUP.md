# AI Assistant Setup

Your exam center now includes a free AI assistant powered by Google's Gemini API!

## Setup Instructions

1. **Get a free Gemini API key:**
   - Visit: https://aistudio.google.com/app/apikey
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy your API key

2. **Add the API key to your environment:**
   ```bash
   # Create a .env.local file in the frontend folder
   cp .env.example .env.local
   
   # Edit .env.local and add your API key:
   NEXT_PUBLIC_GEMINI_API_KEY=your_actual_api_key_here
   ```

3. **Restart your development server:**
   ```bash
   npm run dev
   ```

## Features

- **Smart Study Assistant**: Ask questions about concepts without getting direct answers
- **Context Aware**: Knows what question you're working on and your certification topic
- **Conversation Memory**: Remembers your conversation within each session
- **Quick Prompts**: Pre-built prompts for common study needs
- **Side Panel UI**: Doesn't interfere with your quiz experience

## Free Tier Limits

Google's Gemini API free tier includes:
- 15 requests per minute
- 1 million tokens per month
- Rate limiting for fair usage

This should be more than enough for study assistance!

## Usage Tips

- Ask for concept explanations rather than direct answers
- Request study strategies and memory techniques  
- Get practice questions generated for your topics
- Ask for clarification on complex topics

## Security Note

The API key is prefixed with `NEXT_PUBLIC_` which means it's visible in the browser. For production applications with sensitive data, consider implementing server-side API calls instead.
