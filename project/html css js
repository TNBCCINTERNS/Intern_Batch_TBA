<!DOCTYPE html>
<html>
<head>
  <title></title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
       <link rel="stylesheet" href="qu.css" />
       <script type="text/javascript" src="cl.js"></script>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Quiz</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Java Test<span class="sr-only">(current)</span></a>
      </li>
    </ul>
    <div class="container" id="sim-progress">
    <div class="progress progress-striped active sim-pro">
      <div class="progress-bar" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: 80%"><span class="sr-only">45% Complete</span>

        </div>
    </div>
</div>
    <form class="form-inline my-2 my-lg-0">


      <button class="btn btn-success my-2 my-sm-0" type="submit">Submit</button>
    </form>
  </div>
</nav>


  <div class="row">
    <div class="col-4">
      <div class="jumbotron">
     <div class="container">
      <h3>Questions</h3><br><div>Test Ends in <span id="time">10:00</span> minutes</div>
      <br>
      <div class="scrollable">
      <div class="list-group">
  <button type="button" class="list-group-item list-group-item-action">Question 2</button>
  <button type="button" class="list-group-item list-group-item-action">Question 3</button>
  <button type="button" class="list-group-item list-group-item-action">Question 4</button>
  <button type="button" class="list-group-item list-group-item-action">Question 5</button>
   <button type="button" class="list-group-item list-group-item-action">Question 5</button>
    <button type="button" class="list-group-item list-group-item-action">Question 5</button>
     <button type="button" class="list-group-item list-group-item-action">Question 5</button>
      <button type="button" class="list-group-item list-group-item-action">Question 5</button>
       <button type="button" class="list-group-item list-group-item-action">Question 5</button>
        <button type="button" class="list-group-item list-group-item-action">Question 5</button>
         <button type="button" class="list-group-item list-group-item-action">Question 5</button>
          <button type="button" class="list-group-item list-group-item-action">Question 5</button>
           <button type="button" class="list-group-item list-group-item-action">Question 5</button>
            <button type="button" class="list-group-item list-group-item-action">Question 5</button>

</div></div></div><br><p>No Of Questions attempted: <span id="acc"> 0</span></p><br><p>No Of Questions Not attempted:<span id="not"> 0</span></p></div></div>
    <div class="col-8"><div class="container">
      <div id="game" class="justify-center flex-column">
        <br><br>
        <h2 id="question">What is the answer to this questions?</h2>
        <br>
        <div class="choice-container">
          <p class="choice-prefix">A</p>
          <p class="choice-text" data-number="1">a</p>
        </div>
        <div class="choice-container">
          <p class="choice-prefix">B</p>
          <p class="choice-text" data-number="2">b</p>
        </div>
        <div class="choice-container">
          <p class="choice-prefix">C</p>
          <p class="choice-text" data-number="3">c</p>
        </div>
        <div class="choice-container">
          <p class="choice-prefix">D</p>
          <p class="choice-text" data-number="4">d</p>
        </div>
      
      <br><br>
       <button class="btn btn-outline-success my-2 my-lg-0 float-right" onclick="getNewQuestion()">Next</button>
    </div></div>
  </div>
</div>
 
 
   <script type="text/javascript" src="quiz.js"></script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>

css

.choice-container {
  display: flex;
  margin-bottom: 0.5rem;
  width: 100%;
  font-size: .75rem;
  border: 0.1rem solid rgb(86, 165, 235, 0.25);
  background-color: white;
}

.choice-container:hover {
  cursor: pointer;
  box-shadow: 0 0.4rem 1.4rem 0 rgba(86, 185, 235, 0.5);
  transform: translateY(-0.1rem);
  transition: transform 150ms;
}

.choice-prefix {
  padding: 1.5rem 2.5rem;
  background-color: #56a5eb;
  color: white;
}

.choice-text {
  padding: 1.5rem;
  width: 100%;
}

.scrollable {
    height: 400px;
    overflow-y: auto;
}

#dr
{
  background-color:grey;
  height:100%;
}


js

const question = document.getElementById("question");
const choices = Array.from(document.getElementsByClassName("choice-text"));
let acc=document.querySelector("#acc");
let ncc=document.querySelector("#not");
let currentQuestion = {};
let acceptingAnswers = false;
let score = 0;
let questionCounter = 0;
let availableQuesions = [];
let k=0;
let nc;
let questions = [
  {
    question: "Inside which HTML element do we put the css?",
    choice1: "<script>",
    choice2: "<javascript>",
    choice3: "<link>",
    choice4: "<li>",
    answer: 3
  },
  {
    question:
      "What is the correct syntax for referring to an external script called 's.js'?",
    choice1: "<script href='s.js'>",
    choice2: "<script name='s.js'>",
    choice3: "<script src='s.js'>",
    choice4: "<script file='s.js'>",
    answer: 3
  },
  {
    question: " How do you write 'Hello World' in a console?",
    choice1: "msgBox('Hello World');",
    choice2: "alertBox('Hello World');",
    choice3: "console.log('Hello World');",
    choice4: "alert('Hello World');",
    answer: 3
  }
];

//CONSTANTS
const CORRECT_BONUS = 10;
const MAX_QUESTIONS = 3;
  nc=MAX_QUESTIONS;
startGame = () => {
  questionCounter = 0;
  score = 0;

  ncc.textContent=nc;
  availableQuesions = [...questions];
  getNewQuestion();
};

getNewQuestion = () => {
  if (availableQuesions.length === 0 || questionCounter >= MAX_QUESTIONS) {
    //go to the end page
    return window.location.assign("/end.html");
  }
  questionCounter++;
  const questionIndex = Math.floor(Math.random() * availableQuesions.length);
  currentQuestion = availableQuesions[questionIndex];
  question.innerText = currentQuestion.question;

  choices.forEach(choice => {
    const number = choice.dataset["number"];
    choice.innerText = currentQuestion["choice" + number];
  });

  availableQuesions.splice(questionIndex, 1);
  acceptingAnswers = true;
};

choices.forEach(choice => {
  choice.addEventListener("click", e => {
    if (!acceptingAnswers) return;
   
   k++;
   acc.textContent=k;
   ncc.textContent=nc-1;
    acceptingAnswers = false;
    const selectedChoice = e.target;
    const selectedAnswer = selectedChoice.dataset["number"];

    const classToApply =
      selectedAnswer == currentQuestion.answer ? "correct" : "incorrect";
      console.log(selectedAnswer)
    setTimeout(() => {
      selectedChoice.parentElement.classList.remove(classToApply);
      getNewQuestion();
    }, 100);
  });
});

startGame();
