(() => {
  const button = document.querySelector("#copy-install");
  const command = document.querySelector("#install-command");
  const status = document.querySelector("#copy-status");

  if (!button || !command || !status) return;

  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(command.textContent.trim());
      status.textContent = "Copied. Ready to paste.";
      button.setAttribute("aria-label", "Install command copied to clipboard");
    } catch {
      status.textContent = "Select the command above and copy it.";
    }
  });
})();
