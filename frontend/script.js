let parsedText = "";
let customizedJson = {};

document.getElementById("upload-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("cv-file");
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("/upload", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  parsedText = data.text;
  alert("CV uploaded and parsed successfully!");
});

document.getElementById("customize-btn").addEventListener("click", async () => {
  const jobRole = document.getElementById("job-role").value;
  const jobDesc = document.getElementById("job-desc").value;

  const res = await fetch("/customize", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ cv_text: parsedText, job_role: jobRole, job_desc: jobDesc })
  });

  const data = await res.json();
  customizedJson = JSON.parse(data.customized_json);
  showEditor(customizedJson);
});

function showEditor(json) {
  const editor = document.getElementById("editor");
  const container = document.getElementById("json-editor");
  container.innerHTML = "";
  editor.classList.remove("hidden");

  Object.keys(json).forEach((key) => {
    const div = document.createElement("div");

    const label = document.createElement("label");
    label.textContent = key;
    label.className = "block font-semibold";

    const textarea = document.createElement("textarea");
    textarea.value = json[key];
    textarea.className = "w-full border px-2 py-1 rounded";
    textarea.rows = 4;
    textarea.dataset.key = key;

    div.appendChild(label);
    div.appendChild(textarea);
    container.appendChild(div);
  });
}

document.getElementById("download-btn").addEventListener("click", async () => {
  const textareas = document.querySelectorAll("#json-editor textarea");
  textareas.forEach((ta) => {
    customizedJson[ta.dataset.key] = ta.value;
  });

  const res = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(customizedJson)
  });

  const blob = await res.blob();
  const link = document.createElement("a");
  link.href = window.URL.createObjectURL(blob);
  link.download = "customized_cv.pdf";
  link.click();
});
