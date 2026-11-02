const form = document.querySelector("#emotion-form");
const statement = document.querySelector("#statement");
const count = document.querySelector("#character-count");
const button = document.querySelector("#analyze-button");
const result = document.querySelector("#result");
const dominantEmotion = document.querySelector("#dominant-emotion");
const resultMessage = document.querySelector("#result-message");
const errorMessage = document.querySelector("#error-message");

statement.addEventListener("input", () => {
  count.textContent = `${statement.value.length} / 2000`;
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.hidden = true;
  errorMessage.hidden = true;
  button.disabled = true;
  button.querySelector("span:first-child").textContent = "Analyzing...";

  try {
    const query = new URLSearchParams({ textToAnalyze: statement.value });
    const response = await fetch(`/emotionDetector?${query}`);
    const message = await response.text();
    if (!response.ok) {
      throw new Error(message);
    }

    const match = message.match(/The dominant emotion is ([^.]+)\./);
    dominantEmotion.textContent = match ? match[1] : "Analysis complete";
    resultMessage.textContent = message;
    result.hidden = false;
  } catch (error) {
    errorMessage.textContent = error.message || "Unable to analyze this statement. Please try again.";
    errorMessage.hidden = false;
  } finally {
    button.disabled = false;
    button.querySelector("span:first-child").textContent = "Analyze emotion";
  }
});