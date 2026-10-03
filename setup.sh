#!/bin/bash
# DarazBD Clone — One-command setup script
# Run: bash setup.sh

set -e
BOLD='\033[1m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

ROOT="$(cd "$(dirname "$0")" && pwd)"

echo -e "\n${CYAN}${BOLD}🚀 DarazBD Clone — Setup${NC}\n"

# ── Backend ──────────────────────────────────────────────────────────────────
echo -e "${BOLD}[1/4] Setting up Python backend...${NC}"
cd "$ROOT/backend"

# Create virtual env if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "  ${GREEN}✓ Created Python venv${NC}"
fi

# Activate and install
source venv/bin/activate
pip install --quiet -r requirements.txt
echo -e "  ${GREEN}✓ Installed Python dependencies${NC}"

# Create uploads dir
mkdir -p uploads
echo -e "  ${GREEN}✓ Created uploads/ directory${NC}"

# Create .env with a random JWT secret if missing
if [ ! -f ".env" ]; then
    cp .env.example .env
    SECRET="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
    sed -i.bak "s|^JWT_SECRET_KEY=.*|JWT_SECRET_KEY=${SECRET}|" .env && rm -f .env.bak
    echo -e "  ${GREEN}✓ Created backend/.env (set ADMIN_EMAIL / ADMIN_PASSWORD in it)${NC}"
fi

deactivate

# ── Frontend ─────────────────────────────────────────────────────────────────
echo -e "\n${BOLD}[2/4] Setting up React frontend...${NC}"
cd "$ROOT/frontend"

if command -v npm &> /dev/null; then
    npm install --silent
    echo -e "  ${GREEN}✓ Installed npm dependencies${NC}"
else
    echo -e "  ${YELLOW}⚠ npm not found. Install Node.js from https://nodejs.org then run: cd frontend && npm install${NC}"
fi

echo -e "\n${BOLD}[3/4] Database will be seeded on first backend start${NC}"
echo -e "  ${GREEN}✓ 50 mock products across 5 categories will be loaded${NC}"

echo -e "\n${BOLD}[4/4] Setup complete!${NC}"
echo -e "\n${CYAN}${BOLD}To start the app:${NC}"
echo ""
echo -e "  ${BOLD}Terminal 1 — Backend:${NC}"
echo -e "    cd backend"
echo -e "    source venv/bin/activate"
echo -e "    uvicorn main:app --reload --port 8000"
echo ""
echo -e "  ${BOLD}Terminal 2 — Frontend:${NC}"
echo -e "    cd frontend"
echo -e "    npm run dev"
echo ""
echo -e "  ${BOLD}Open:${NC} http://localhost:5173"
echo -e "  ${BOLD}API Docs:${NC} http://localhost:8000/docs"
echo ""
