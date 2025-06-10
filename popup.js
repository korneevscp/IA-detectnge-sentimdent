chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  const tab = tabs[0];
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => {
      return window.getSelection().toString() || document.body.innerText.slice(0, 1500);
    }
  }, (injectionResults) => {
    const content = injectionResults[0].result;

    fetch("http://localhost:5000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: content })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("result").innerHTML = `
        <p><strong>Résumé :</strong> ${data.summary}</p>
        <p>🎯 <strong>Intention :</strong> ${data.intention}</p>
        <p>💡 <strong>Émotion dominante :</strong> ${data.emotion}</p>
        <p>📊 <strong>Objectivité estimée :</strong> ${data.objectivity}%</p>
        <p>🔁 <strong>Source opposée :</strong> <a href="${data.alt_source}" target="_blank">${data.alt_label}</a></p>
      `;
    })
    .catch(err => {
      document.getElementById("result").innerHTML = `<p>Erreur : ${err.message}</p>`;
    });
  });
});
// popup.js