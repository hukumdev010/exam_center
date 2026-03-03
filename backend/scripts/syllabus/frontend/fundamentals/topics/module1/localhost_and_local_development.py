"""
Localhost and Local Development - Detailed Content

This file contains content for the "Localhost and Local Development" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Localhost and Local Development",
    "duration": "8-10 minutes",
    "difficulty": "Beginner",
    "overview": """
    Localhost is your local computer acting as a web server during development. Understanding how to run
    a development server on your machine is essential for testing before deploying to production.
    """,
    
    "detailed_content": {
        "introduction": """
When you build a web application, you don't immediately deploy it to the internet. Instead, you develop and test
it locally on your own computer. Your computer acts as both the client (browser) and server, allowing you to test
your application before anyone else sees it. This is called local development, and it's where you spend most of
your development time.
        """,
        
        "key_concepts": {
            "what_is_localhost": """
**Localhost Explained**

Localhost is a special address that means "this computer." In your browser, typing `localhost` or `127.0.0.1`
connects to a server running on your own machine.

**Common localhost URLs**:
- `http://localhost:3000` - React development server
- `http://localhost:10000` - Django development server
- `http://localhost:5000` - Flask development server
- `http://127.0.0.1:3000` - Same as localhost:3000

**Port Numbers**

The number after the colon (like 3000, 10000) is the port. It's like a channel on your computer. You can run
multiple servers simultaneously on different ports.

**How It Works**

1. Start a development server on your machine
2. The server listens on localhost:PORT
3. Open browser and navigate to localhost:PORT
4. Browser connects to your local server
5. Server sends files and handles requests
6. You see your application

**Only You Can Access It**

By default, only you can access localhost. Others can't visit `localhost:3000` on their browsers—it would try
to connect to their own computer, not yours.
            """,
            
            "setting_up_servers": """
**Starting a Development Server**

Different tools start servers differently:

**Node.js/npm Projects**:
```bash
npm start          # Runs dev script from package.json
npm run dev        # Run dev script
```

**Python Flask**:
```bash
flask run
python app.py
```

**Python Django**:
```bash
python manage.py runserver
```

**Live Server (VS Code)**:
Right-click HTML file and select "Open with Live Server"

**Node.js Direct**:
```bash
node server.js
```

**Common Development Servers**:
- **npm/Node.js**: Vite, Webpack Dev Server, Create React App
- **Python**: Flask development server, Django development server
- **Ruby**: Rails development server
- **PHP**: PHP built-in server

**Auto-Reload**

Most development servers automatically reload when you save files. This is called "hot reload" or "live reload."
You change code, save, and instantly see changes in the browser without manual refresh.
            """,
            
            "typical_workflow": """
**Development Loop**

1. **Start server**: `npm start`
2. **Open browser**: Navigate to `localhost:3000`
3. **Edit code**: Change a file in your editor
4. **Browser reloads**: See changes instantly
5. **Debug**: Use DevTools if something's wrong
6. **Repeat**: Continue developing

**Accessing From Other Devices**

To test on other devices on the same network:

```bash
# Find your local IP (macOS/Linux)
ifconfig | grep inet

# Find your local IP (Windows)
ipconfig
```

Then visit `http://YOUR_IP:3000` from another device on the same network.

**Simulating Slow Networks**

In DevTools Network tab:
1. Click the network speed dropdown (usually "No throttling")
2. Select "Fast 3G", "Slow 3G", or "Offline"
3. Test how your app performs on slow connections

**Environment Variables**

During development, you often use different settings than production:

```bash
# .env.local (development)
API_URL=http://localhost:3001
DATABASE_URL=localhost:5432

# .env.production (production)
API_URL=https://api.production.com
DATABASE_URL=prod-database.com
```
            """,
            
            "common_issues": """
**Port Already in Use**

Error: "Port 3000 is already in use"

Solution:
```bash
# Find what's using port 3000
lsof -i :3000          # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Kill the process
kill -9 PID            # macOS/Linux
taskkill /PID <PID>    # Windows

# Or use a different port
npm start -- --port 3001
```

**Cannot Connect to Server**

- Check if server is actually running
- Verify correct port number
- Check for error messages in terminal
- Restart the server

**Files Not Updating**

- Make sure server has auto-reload enabled
- Check file is actually saved
- Hard refresh browser (Ctrl+Shift+R)
- Restart server if auto-reload broken

**CORS Errors**

When frontend and backend are on different ports:
- Frontend: `localhost:3000`
- Backend: `localhost:3001`

Backend needs to allow requests from frontend. Backend developer configures CORS.
            """,
            
            "best_practices": """
**Keep Development Organized**

- Use same folder structure as production
- Test across different browsers
- Regularly check DevTools console for errors
- Use meaningful environment variables
- Document how to start the dev server

**Testing Tips**

- Test on mobile devices (use local IP)
- Test with slow networks (DevTools throttling)
- Clear cache if seeing old files
- Test with JavaScript disabled
- Test keyboard navigation

**Security in Development**

- Don't commit sensitive credentials
- Use .env files for secrets
- Don't share localhost ports publicly
- Keep dependencies updated
            """
        }
    },
    
    "key_takeaways": [
        "Localhost means your own computer acting as a server",
        "Port numbers allow multiple servers on one computer",
        "Development servers auto-reload when you save",
        "Only you can access localhost by default",
        "Use environment variables for different settings",
        "Test on other devices using local IP address",
        "DevTools throttling simulates slow networks"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Start a development server and visit localhost",
            "Change a file and see auto-reload in action",
            "Try different port numbers",
            "Find your local IP and test from phone",
            "Use DevTools to simulate slow networks",
            "Check environment variables in your project"
        ]
    },
    
    "related_topics": [
        "Production vs Development",
        "Command Line Basics",
        "Developer Tools and DevTools"
    ]
}
