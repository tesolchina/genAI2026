
Vanderbilt University
Claude Code: Software Engineering with Generative AI Agents
Introduction to Claude Code & Software Engineering with AI Agents
Video. Duration: 7 minutes7 min
1000X Improvement in Software Engineering Productivity with Big Prompts
Video. Duration: 12 minutes12 min
An Important Note on Costs
Reading. Duration: 10 minutes10 min
Exercise: Getting Started with Claude Code & Building Your First Application
Reading. Duration: 10 minutes10 min
Learning More & Staying Connected
Reading. Duration: 1 minute1 min
Exercise: Getting Started with Claude Code & Building Your First Application
0:03
/
4:29
Prerequisites
Basic familiarity with command line/terminal

If you need help, open 
Claude
 and prompt it with: "Teach me how to use the command line on my system. Ask me one question at a time or tell me one step at a time what to do. What is the first question or step?"

Node.js installed on your system (
https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
)

If you need help, open 
Claude
 and prompt it with: "Help me install NodeJS and NPM. Ask me one question at a time or tell me one step at a time what to do. What is the first question or step?"

Git installed and configured

If you need help, open 
Claude
 and prompt it with: "Help me install the Git CLI. Ask me one question at a time or tell me one step at a time what to do. What is the first question or step?"

Part 1: Installing Claude Code
Step 1: Installation
To get access to Claude Code:

Get Access: Visit 
claude.ai/code
 to sign up for a subscription that includes Claude Code or get an API key to pay for usage

Install via npm (once you have access): npm install -g @anthropic-ai/claude-code

Verify Installation: claude --version

Step 2: First Launch
Create a new project directory: mkdir expense-tracker-ai 

Change to the project directory:  cd expense-tracker-ai

Launch Claude Code: claude

First-time setup: Claude will prompt you to authenticate and set up basic permissions.

Part 2: Understanding the Interface
Key Interface Elements
When you launch Claude Code, you'll see:

Prompt input: Where you type your instructions

Tool permission requests: Claude will ask before running commands

File operations: You'll see real-time file creation and editing

Todo updates: Claude explains what it's doing as it works

Essential Commands
/init: Initialize a CLAUDE.md file for your project (when there is an existing project)

/permissions: Manage tool permissions

/clear: Clear conversation history

/help: Show available commands

Slash commands: Type / to see all available commands

Part 3: Your First Big Prompt - Building an Expense Tracker
Step 1: Initialize the Project with The Big Prompt Approach
Instead of asking Claude to "create a component" or "add a function," we're going to use a big prompt that describes our entire vision. This is the key to leveraging AI as labor rather than just a coding assistant.

41
I want you to create a modern, professional NextJS expense tracking application. Here's my vision:

APPLICATION OVERVIEW:
Build a complete expense tracking web app that helps users manage their personal finances. The app should feel modern, intuitive, and professional.

CORE FEATURES:
- Add expenses with date, amount, category, and description
- View expenses in a clean, organized list
- Filter expenses by date range and category
- Dashboard with spending summaries and basic analytics

Step 3: Watch Claude Work
After sending this prompt, Claude will:

Plan the approach: It will outline how it will build the application

Create the project structure: Set up NextJS with TypeScript and Tailwind

Build components: Create all the necessary React components

Implement features: Add all the functionality you requested

Test and verify: Make sure everything works together (it may forget to do this...if so, remind it with something like "please compile and make sure the application runs...")

Important: Claude will ask for permissions to:

Run terminal commands (npm create-next-app, npm install, etc.)

Create and edit files

Install dependencies

Always review what it's asking to do and approve safe operations.

Step 4: Understanding the Output
As Claude works, pay attention to:

File structure: How it organizes the project

Component architecture: How it breaks down the application

State management: How it handles data flow

Styling approach: How it implements the design

Step 5: Testing Your Application
Once Claude finishes, it will provide instructions to run the app:

npm run dev

Open your browser to http://localhost:3000 and test.

Part 4: Understanding What Just Happened
The Power of Big Prompts
What you just experienced is fundamentally different from traditional coding:

Vision-Level Instructions: Instead of writing code, you described your vision

Complete Implementation: Claude built an entire application, not just pieces

Holistic Approach: It considered architecture, design, and user experience together

Professional Quality: The result should be production-ready code

AI as Labor, Not Just a Tool
This demonstrates the core concept from the course:

Traditional approach: "Write me a function to calculate totals"

AI Labor approach: "Build me a complete expense tracking application"

Human Time Efficiency
Notice how much you got for a single prompt:

Complete NextJS application

Multiple components and features

Professional styling

Type safety and validation

Responsive design






