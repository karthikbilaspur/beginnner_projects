// Get elements

const quizContainer = document.getElementById('quiz-container');
const questionElement = document.getElementById('question');
const optionsElement = document.getElementById('options');
const submitButton = document.getElementById('submit-button');
const resultsContainer = document.getElementById('results-container');
const scoreElement = document.getElementById('score');

// Quiz variables

let currentQuestion = 0;
let score = 0;

// Quiz functions

function showQuestion() {
  const question = questions[currentQuestion];
  questionElement.textContent = question.text;
  optionsElement.innerHTML = '';
  question.options.forEach((option, index) => {
    const radio = document.createElement('input');
    radio.type = 'radio';
    radio.name = 'option';
    radio.value = index;
    const label = document.createElement('label');
    label.textContent = option;
    optionsElement.appendChild(radio);
    optionsElement.appendChild(label);
    optionsElement.appendChild(document.createElement('br'));
  });
}

function checkAnswer() {
  const selectedOption = document.querySelector('input[name="option"]:checked');
  if (selectedOption) {
    const question = questions[currentQuestion];
    if (parseInt(selectedOption.value) === question.answer) {
      score++;
    }
  }
}

function showResults() {
  quizContainer.style.display = 'none';
  resultsContainer.style.display = 'block';
  scoreElement.textContent = `Score: ${score} / ${questions.length}`;
}

// Event listeners

submitButton.addEventListener('click', () => {
  checkAnswer();
  currentQuestion++;
  if (currentQuestion >= questions.length) {
    showResults();
  } else {
    showQuestion();
  }
});

// Initialize quiz

showQuestion();