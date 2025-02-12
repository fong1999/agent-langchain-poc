# AgentLangchain

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 19.1.6.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Karma](https://karma-runner.github.io) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.

🔹 Frontend: Angular Setup


## Set PATH

```
export PATH="/opt/homebrew/opt/node@20/bin:$PATH"
```
## Clean

```
rm -rf node_modules package-lock.json .angular/cache
rm -rf node_modules package-lock.json  # ✅ Remove old dependencies
npm install                            # ✅ Reinstall fresh dependencies

ng serve --open
```

1️⃣ Create an Angular project

```
ng new agent-playground-langchain --style=scss --routing
cd agent-playground-langchain
```

2️⃣ Install Angular dependencies

```
npm install @angular/material @angular/flex-layout
npm install axios  # For calling the Python backend
```

3️⃣ Create a Chat Component

```
ng generate component components/chat
```
Backend: Python + LangChain Setup
1️⃣ Create a Python virtual environment

```
mkdir agent-playground-langchain-backend && cd agent-playground-langchain-backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2️⃣ Install dependencies

```
pip install fastapi uvicorn langchain openai requests
```


