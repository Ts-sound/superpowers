# Create virtual environment and install dependencies

Write-Host "Creating Python virtual environment..." -ForegroundColor Green

python -m venv .venv
& .\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Installing dev tools..." -ForegroundColor Green
pip install pytest pytest-cov

Write-Host "Installing build tools..." -ForegroundColor Green
pip install pyinstaller

Write-Host "Environment setup complete!" -ForegroundColor Green
Write-Host "To activate: .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow