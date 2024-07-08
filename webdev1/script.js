const quizQuestions = [
    {
        question: "What is the fastest swimming stroke?",
        options: ["Freestyle", "Butterfly", "Backstroke", "Breaststroke"],
        answer: "Freestyle"
    },
    {
        question: "How many individual medley events are in the Olympics?",
        options: ["2", "3", "4", "5"],
        answer: "2"
    },
    {
        question: "What is the length of an Olympic swimming pool?",
        options: ["25 meters", "50 meters", "100 meters", "200 meters"],
        answer: "50 meters"
    },
    {
        question: "Who holds the record for most Olympic gold medals in swimming?",
        options: ["Ian Thorpe", "Michael Phelps", "Mark Spitz", "Katie Ledecky"],
        answer: "Michael Phelps"
    },
    {
        question: "Which country has won the most gold medals in swimming?",
        options: ["Australia", "China", "USA", "Germany"],
        answer: "USA"
    }
];

let currentQuestionIndex = 0;
let score = 0;

function loadQuestion() {
    const questionNumberContainer = document.getElementById('question-number');
    const questionContainer = document.getElementById('quiz-question');
    const optionsContainer = document.getElementById('quiz-options');
    const feedbackContainer = document.getElementById('feedback');
    const nextButton = document.getElementById('next-button');
    const restartButton = document.getElementById('restart-button');

    feedbackContainer.innerHTML = '';
    nextButton.style.display = 'none';

    const currentQuestion = quizQuestions[currentQuestionIndex];
    questionNumberContainer.innerHTML = `Question ${currentQuestionIndex + 1} of ${quizQuestions.length}`;
    questionContainer.innerHTML = currentQuestion.question;
    optionsContainer.innerHTML = '';

    currentQuestion.options.forEach(option => {
        const button = document.createElement('div');
        button.classList.add('option');
        button.innerText = option;
        button.onclick = () => checkAnswer(button, option);
        optionsContainer.appendChild(button);
    });

    if (currentQuestionIndex > 0) {
        restartButton.style.display = 'inline-block';
    }
}

function checkAnswer(button, selectedOption) {
    const feedbackContainer = document.getElementById('feedback');
    const nextButton = document.getElementById('next-button');
    const currentQuestion = quizQuestions[currentQuestionIndex];

    if (selectedOption === currentQuestion.answer) {
        feedbackContainer.innerHTML = 'Correct!';
        button.classList.add('correct');
        score++;
    } else {
        feedbackContainer.innerHTML = 'Wrong!';
        button.classList.add('wrong');
    }

    document.querySelectorAll('.option').forEach(option => {
        option.onclick = null;
    });

    nextButton.style.display = 'inline-block';
}

function loadNextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < quizQuestions.length) {
        loadQuestion();
    } else {
        showResults();
    }
}

function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    loadQuestion();
}

function showResults() {
    const questionNumberContainer = document.getElementById('question-number');
    const questionContainer = document.getElementById('quiz-question');
    const optionsContainer = document.getElementById('quiz-options');
    const feedbackContainer = document.getElementById('feedback');
    const nextButton = document.getElementById('next-button');
    const restartButton = document.getElementById('restart-button');

    questionNumberContainer.innerHTML = '';
    questionContainer.innerHTML = 'Quiz Completed!';
    optionsContainer.innerHTML = `Your score: ${score} out of ${quizQuestions.length}`;
    feedbackContainer.innerHTML = '';
    nextButton.style.display = 'none';
    restartButton.style.display = 'inline-block';
}

// Initialize the quiz
loadQuestion();
