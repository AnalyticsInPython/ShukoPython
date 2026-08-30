# ENGI 4503: Analytics in Python (MBAxMS)

A five-day, twenty-hour bootcamp on programming and working with data in Python alongside a coding agent (we'll use Claude Code).
We'll introduce Polars for cleaning, manipulating, filtering and analyzing data.
We'll exercise those skills on real datasets.
By the end of the week, each group will demo a working web application with a Python backend and a data-analysis component, built largely by directing an agent.

Our emphasis will not be on you writing code by hand.
It will be on:

  * understanding what the agent is doing,
  * reading and understanding the Python it produces to the best of our abilities,
  * specifying intent precisely enough that it builds the right thing,
  * recognizing and intervening when it's going off the rails -- wrong abstractions, invented APIs, flaky tests, runaway cost,
  * and developing the judgment to direct it well.

Reading code and having a good design mindset are the load-bearing skills here, but building your own technical expertise matters just as much, so that you are never fully reliant on the agent getting everything right on its own.
An agent that writes code you cannot read is a machine for producing confident, plausible, unverifiable work.

It's important to get frustrated at least once as part of the course!
"Frustrated" here means to attempt to solve a programming problem that you do not already feel comfortable solving today, to work at it as best of your abilities and then to ask for help getting over the finish line.

## Course Details

*Dates*: Monday August 31 - Friday September 4, 2026

*Time*: 13:00-17:30, except Friday September 4, which is 13:00-15:00

*Room*: Tang Family Hall, Columbia Engineering Innovation Hub, 2276 12th Avenue, Floor 2

### Instructor

[Julian Berman `<julian.berman@columbia.edu>`](mailto:julian.berman@columbia.edu)

## Prerequisites

You are assumed to have written some code before -- roughly one semester, ideally in Python -- and to have used a large language model through a chat interface.

You are *not* assumed to have used a coding agent, the command line, or git and GitHub for real work.
We start from the beginning on those three.

### Opting Out

This course is a bootcamp.
You probably don't need it if you can already:

  * ship a small web application end-to-end (frontend + backend + database) on your own,
  * read a non-trivial PR diff and explain what's wrong with it,
  * name what's in a `pyproject.toml`, what a virtualenv is, what a branch is, and what a flaky test is,
  * and use a coding agent daily for real work.

If two or more of those feel uncertain, stay.

To opt out, send me an example of a project you've built -- ideally something resembling a small web application or analysis tool -- along with a brief note on what was yours, what was an agent's, and what you learned.

## For the First Day

A few things to get set up with beforehand.
We'll sort out whatever didn't work on the first day.

  * Install [Claude](https://claude.com/download) for *all three* of Desktop, Terminal and VSCode
  * Install [VSCode](https://code.visualstudio.com/download)
  * Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/), which we'll use to run Python and to manage packages
  * [Sign up](https://github.com/signup) for a GitHub account, and [install the GitHub command line program](https://cli.github.com/).
    You'll want to sign up for [their Student benefits](https://github.com/education/students)

The school is providing a budget of tokens for use with Claude.
Details on getting set up with it will be given in class.

## Schedule

|  Day | Duration | Focus                                        | Project time |
|------|----------|----------------------------------------------|--------------|
|  1   | 4.5 hr   | Fundamentals of Python and agentic coding    | ~45 min      |
|  2   | 4.5 hr   | APIs, web applications, and other interfaces | ~90 min      |
|  3   | 4.5 hr   | Cleaning and analyzing real data             | ~90 min      |
|  4   | 4.5 hr   | Iteration, testing, and checking answers     | ~90 min      |
|  5   | 2 hr     | Group demos                                  | --           |

Each of Days 1-4 runs as three working blocks with a fifteen-minute break after each, followed by group project work in class -- ninety minutes on Days 2 through 4, and forty-five on Day 1 for forming groups and getting started.
Day 5 is demos only.

**Day 1 -- Fundamentals of Python and agentic coding.**
What an agent loop is and what it replaced; what you're paying for when one runs.
We'll have an agent write real Python and then spend much of the day reading it: what the files do, what the pieces are called, how to read a traceback, and where the agent got something subtly wrong.
We'll also cover the ways you can run Python at all -- as a script, in the REPL, and in a notebook.

**Day 2 -- APIs, web applications, and other interfaces.**
How data gets into a program from outside -- HTTP, REST and JSON -- and where it goes once you have it: why databases exist, and SQLite.
Where an analysis surfaces its answer: standard output, a terminal, a notebook, or a web page.
The anatomy that follows from choosing the last of those -- frontend, backend, database, hosting -- and where the agent writes which language.
Git and GitHub, and how to describe what you want well enough to get it.

**Day 3 -- Cleaning and analyzing real data.**
Real data arrives dirty, and most of the work in an analysis happens before the analysis does.
What that looks like -- missing values, duplicates, wrong types, and rows that aren't the thing you think they are -- and dataframes with Polars as the instrument for fixing it.
We'll take a public dataset large enough that a spreadsheet struggles and clean it in a notebook, in three groups that each hand the agent a different share of the judgment involved, compare what came back, and then answer a real question with the result.

**Day 4 -- Iteration, testing, and checking answers.**
Almost no real work is written from nothing; it is changing code that already exists without breaking it.
We'll add real functionality to something we've already built, and cover the kinds of tests that make that safe to attempt.
We'll also look at how analyses go wrong -- the confident, plausible, wrong answer -- and at how you catch one before you present it.

**Day 5 -- Demos.**
Each group demonstrates what they built, live, followed by questions.

The pace of the course may be slow for some and fast for others for the first day or two, depending on your level of prior knowledge.
Programming, data analysis and machine learning are, unsurprisingly, immense fields of study.
Effort will be made to provide additional resources throughout the course, should you wish to deepen your understanding of a particular topic.
Investing additional time in areas that interest you is of course encouraged.
Feel free to raise any additional topics which interest you.

## The Group Project

The project runs the length of the week and is the main thing you'll be evaluated on.

  * Groups of 3-4, self-picked.
  * The deliverable is a web application with a Python backend.
  * It must include a data-analysis component. This can be auxiliary rather than central -- analyzing your application's own usage or content counts.
  * The data-analysis component should involve some amount of Python. Visualizations within the web application itself may of course be TypeScript or JavaScript.
  * Each group emails a one-page proposal after Day 1: what it does, who it's for, what data it uses, and what question it answers. I'll approve by Day 2 so you can begin work on it.
  * You'll have about ninety minutes of in-class project time on each of Days 2, 3 and 4 to work with your groupmates, and can make use of post-class time as needed.
    Some of Day 4's is for working out what your demo will actually show -- it's the last time you're all in a room with me before you present.
  * On Day 5 you demo it live -- roughly ten minutes including questions -- in whatever format your group chooses (live app walkthrough, slide presentation, interpretive dance, ...).

Dividing up the work is your group's responsibility.
Everyone should make some agentic-coding contribution to what you finally show -- it's the skill the week exists to build, and it isn't one you can pick up by watching a groupmate do it.
If there are concerns about how the work is being shared, try first to settle them within the group, and come to me in cases where that can't or doesn't happen.

Each group creates its own repository on GitHub and shares it with me on Day 2.
All of your work lives there, and its history is part of what I'll look at.

There is no separate homework track.
The work between sessions is the next increment of your own project.

Lectures and your project run in parallel rather than in lockstep.
You'll often apply something days after we cover it, and you'll often want something before we've got to it -- ask, and I'll point you at what you need.

Roughly where you should be by each evening.
Projects differ, so treat these as targets rather than deliverables:

  * After Day 1 -- a group, and a proposal in my inbox.
  * After Day 2 -- a repository, and the smallest version of your application that runs at all, storing the data it fetches.
  * After Day 3 -- something computed from the data your application stores.
  * After Day 4 -- the thing you proposed, working, and a plan for how you'll show it.

## Evaluation

  * Group project (65%).
    Judged on whether the application works, whether the analysis answers a real question and is defensible, the quality of what's in the repository, and the demo.
    A significant part of this is whether your group can explain the code it shipped.
    Expect to be asked about both why it works one way or another as well as how you developed it and how your interactions went.

  * Lowlights One-Pager (20%).
    An individual one-page document, due at the end of the week, on the things you saw go wrong while working with an agent -- on your project or in the exercises.
    For each: how you noticed, what you think actually went wrong, and what you did about it.
    You write this one alone even though the project is a group effort, and two people in the same group shouldn't be handing in the same page.
    It's deliberately about failure rather than about what you shipped. Noticing is the skill this course is trying to build, and this is where you show me you have it.

  * Participation (15%).
    In-class exercises and discussion.
    Exercises are not individually graded; they exist so that you find out what you don't understand while I'm still in the room.
    Come every day -- each day builds on the last, and your group is relying on you.

## Computers in Class

We will spend most of the week programming.
A computer will be required for every lecture.
Please ensure you bring one and that it is well charged.
Any operating system will do -- macOS, Windows or Linux.
I'll do my best to ensure instructions work for your environment, but speak up during the course if you ever run into trouble.
All code I provide should work no matter which operating system you are on.
Tablets are likely not sufficient.

## Getting the Most Out of the Course

The best and only way to learn is to be programming along, not simply watching me do so.
Before you run any code -- mine, yours, or the agent's -- read it and predict what it does.
This skill is itself a primary goal of the course; you'll learn how confidently you can assume your guesses about a program are right.
Intentionally break things at times.
This too helps your mental model.

When the agent hands you something that works, the work isn't finished.
Read it and be able to say what it does before you move on, because you will be asked to.

## Resources

You will not be required to read any of the below cover to cover.
In this course you'll learn Python mostly by reading what an agent wrote and working out what it does, and when you don't understand something the fastest thing to do is ask -- me, or the agent itself.

What follows is for when you want to understand something more deeply than a week allows.
There is an abundance of material available which teaches how to program in Python, and an emerging abundance on agentic coding -- though on that second subject all of us know rather less, both about where it is going and about our own role within it.
You're of course welcome to ask for more materials or information in-class on any topic.

On some days I'll point you at a particular problem or chapter as optional extra practice; it's never graded, and doing it is entirely up to you.

### Python, and analyzing data with it

  * [The official Python tutorial](https://docs.python.org/3/tutorial/index.html), a tutorial which is quite good, albeit which assumes in places that you are familiar with or arriving to Python from a lower-level language, specifically C

  * [Think Python, by Allen B. Downey](https://allendowney.github.io/ThinkPython/), a printed book available for purchase which Downey makes freely available as well, and which is well-regarded

  * [The Polars user guide](https://docs.pola.rs/), which goes considerably further than the day we spend on it

  * Videos from Anthony Sottile, who makes a large number of videos on Python, [many of which are beginner-friendly](https://www.youtube.com/@anthonywritescode/search?query=beginner)

### The tools we're using

  * [Claude Code's documentation](https://docs.claude.com/en/docs/claude-code), worth a skim early in the week -- much of what we cover in class is in there, along with a good deal we won't get to

  * [Anthropic Academy](https://anthropic.skilljar.com/), Anthropic's own free courses. *Claude Code 101* and *Claude Code in Action* are the directly relevant ones, and there is a good deal more there if you want it

  * [GitHub Learn](https://learn.github.com/skills), GitHub's own interactive exercises, which are a gentler way into branches and pull requests than reading about them

### Problems to work through

Exercises and worked examples, if you want more practice than the project gives you.
Work them by hand or with an agent alongside you -- both build the understanding, and comparing what you'd have written to what it writes is worth doing at least once.

  * [Software Design by Example, by Greg Wilson](https://third-bit.com/sdxpy/), a recent text with pragmatic programming examples aimed at teaching programming in a hands-on way

  * [Automate the Boring Stuff, by Al Sweigart](https://automatetheboringstuff.com/#toc), which similar to the above is printed, but which Sweigart makes freely available along with other books he has authored

  * [Peter Norvig's pytudes](https://github.com/norvig/pytudes), "Python programs, usually short, of considerable difficulty, to perfect particular skills."
    which, as the blurb says, are quite challenging problems well beyond the scope of this bootcamp, but which may be enlightening to look at solutions provided to some of the problems

## Taking Notes

Whether and how you take notes or save outputs and projects you build in class is up to you.
A suggestion is: given that the source code for the course is a GitHub repository, you can fork it using the button you'll find in the GitHub UI and make changes to files (by adding your notes).
You can then push those changes to your own fork on GitHub alongside your personal work.
Doing this is definitely a good way to get additional exposure to `git` and GitHub.
Basic details on how to do so will be covered in the first lecture, but feel free to ask if you need more specific instructions.

## Getting Help

Ask for help when you need it, particularly if you don't understand something.
Programming is often cumulative, and if you get lost, it's easy to compound how lost you end up.
Asking for clarification on a topic in-class is always welcome.
You can also email me any time, and particularly between sessions, when you're working on your project and I'm not in the room.

## LLMs & Coding Agents

This course is built around using them, so their use is not only allowed, it is essentially required.
You are expected to use a coding agent for the majority of your project work, and most of what you submit will have been written by one, but you will be expected to be a driver not a passenger.

Specifically:

  * You own everything you submit.
    If it's wrong, it's wrong because you accepted and shared it, not because the model wrote it.
    Not knowing everything is to be expected, but not taking time to dig into your collaborative work with Claude is not.
  * You must be able to explain your project.
    Not having read something before shipping it is the specific failure this course exists to prevent.
  * Watch what it costs.
    We'll cover why agent runs cost what they do and how to keep that under control.
  * Be careful what you paste in.
    Don't put anything into a prompt you wouldn't be comfortable sending to a third party, and don't commit credentials or API keys to your repository.

Do familiarize yourself with the Columbia [academic integrity policies](https://www.cc-seas.columbia.edu/academic-integrity/policy-practices/understanding-policy).

## Inclusion, Accommodations & Support

Columbia University is committed to providing a learning, living, and working environment free from unlawful discrimination and harassment and to fostering a nurturing and vibrant community founded upon the fundamental dignity and worth of all of its members.
The university prohibits any form of discrimination against any person on the basis of race, color, religion, sex, gender, pregnancy, age, national origin, disability, sexual orientation, marital status, status as a victim of domestic violence, citizenship or immigration status, creed, genetic predisposition or carrier status, unemployment status, partnership status, military status, or any other applicable legally protected status in the administration of its educational policies, admissions policies, employment, scholarship and loan programs, and athletic and other University-administered programs and functions.
As members of the community, we have a shared responsibility to uphold these standards and report behavior that violates these standards.
If you need to report a concern or otherwise need support, you may do so [here via the Office of Institutional Equity (OIE)](https://universitylife.columbia.edu/report).
