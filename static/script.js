document.addEventListener("DOMContentLoaded", function() {
  const showFormButton = document.getElementById("showFormButton");
  const showSecondFormButton = document.getElementById("showSecondFormButton");
  const detailsForm = document.getElementById("detailsForm");
  const details2Form = document.getElementById("details2Form");
  //const secondFormContainer = document.getElementById("secondFormContainer");
  const inputForm = document.getElementById("inputForm");
  const secondForm = document.getElementById("secondForm");
  const submittedDetails = document.getElementById("submittedDetails");
  const submittedText = document.getElementById("submittedText");
  const forms = document.getElementById("forms");

  showFormButton.addEventListener("click", function() {
    forms.classList.remove("button", "hidden");
    forms.classList.add("button");
    detailsForm.classList.remove("button", "hidden");
    detailsForm.classList.add("button");
    showFormButton.classList.remove("button", "hidden");
    showFormButton.classList.add("hidden");
  });

  showSecondFormButton.addEventListener("click", function() {
    forms.classList.remove("button", "hidden");
    forms.classList.add("button");
    details2Form.classList.remove("button", "hidden");
    details2Form.classList.add("button");
    showSecondFormButton.classList.remove("button", "hidden");
    showSecondFormButton.classList.add("hidden");
  });

  inputForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const field1Input = document.getElementById("field1").value;
    const field2Input = document.getElementById("field2").value;
    const field3Input = document.getElementById("field3").value;
    const field4Input = document.getElementById("field4").value;

    // Process and display the first form data
    const submittedTextContent = `
      Task Name: ${field1Input}<br>
      Task Description: ${field2Input}<br>
      Deadline: ${field3Input}<br>
      Domain: ${field4Input}
    `;

    submittedText.innerHTML = "Task submitted:<br>" + submittedTextContent;

    submittedDetails.classList.remove("hidden");
    inputForm.classList.add("hidden");
    showFormButton.classList.remove("hidden");
  });

  // Event listener for the second form
  secondForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const field5Input = document.getElementById("field5").value;
    const field6Input = document.getElementById("field6").value;

    // Process and display the second form data
    const submittedTextContent = `
      Name: ${field5Input}<br>
      Domain: ${field6Input}
    `;

    submittedText.innerHTML = "Employee Details submitted:<br>" + submittedTextContent;

    submittedDetails.classList.remove("hidden");
    secondFormContainer.classList.add("hidden");
    showSecondFormButton.classList.remove("hidden");
  });
});
