# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os, sys, time, json, shutil, random, asyncio, platform, subprocess, yaml, re
from pathlib import Path
from datetime import datetime
import httpx
from urllib.parse import urljoin, urlparse

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.formatted_text import FormattedText
    from prompt_toolkit.styles import Style
    from prompt_toolkit.shortcuts import print_formatted_text, CompleteStyle
    from prompt_toolkit.completion import WordCompleter
    PROMPT_TOOLKIT_AVAILABLE = True
except ImportError:
    PROMPT_TOOLKIT_AVAILABLE = False

class Colors:
    RED, GRN, YEL, BLU, MAG, CYN, WHT, GRY, END, BLD, ISLAMIC_GREEN = '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m', '\033[90m', '\033[0m', '\033[1m', '\033[38;5;34m'

class TerminalView:
    def __init__(self):
        self.session = PromptSession(completer=WordCompleter(['/help', '/exit', '/menu'], ignore_case=True), complete_style=CompleteStyle.MULTI_COLUMN) if PROMPT_TOOLKIT_AVAILABLE else None

    def display_banner(self):
        banner = f"""{Colors.CYN}{Colors.BLD}
    ███████╗███████╗ ██████╗██████╗ ██████╗ ██████╗     ██████╗ ██████╗  █████╗  ██████╗
    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ███████╗█████╗  ██║     ██████╔╝██████╔╝██║  ██║    ██████╔╝██████╔╝███████║██║     
    ╚════██║██╔══╝  ██║     ██╔══██╗██╔══██╗██║  ██║    ██╔═══╝ ██╔══██╗██╔══██║██║     
    ███████║███████╗╚██████╗██║  ██║██║  ██║██████╔╝    ██║     ██║  ██║██║  ██║╚██████╗
    ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
    {Colors.YEL}B A L A N C E   B R E A K E R  -  U L T I M A T E   E D I T I O N{Colors.END}"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(banner)
        print(f"\n{Colors.ISLAMIC_GREEN}{Colors.BLD}Bismillah! Welcome, ethical hacker.{Colors.END}\n")

    def display_main_menu(self):
        menu = f"""
        {Colors.YEL}{Colors.BLD}╔═══════════════════════════════ MAIN MENU ═══════════════════════════════╗{Colors.END}
        {Colors.CYN}║{Colors.RED}{Colors.BLD} [N] God-Level Recon (Nuclei) {Colors.END} {Colors.CYN}║{Colors.WHT} [9] 🚪 Exit                       {Colors.CYN}║
        {Colors.CYN}║{Colors.WHT} [1] 💬 AI Command Console    {Colors.CYN}║{Colors.WHT}                                     {Colors.CYN}║
        {Colors.YEL}{Colors.BLD}╚═════════════════════════════════════════════════════════════════════════╝{Colors.END}"""
        print(menu)

    async def get_user_input(self, prompt):
        if self.session:
            return await self.session.prompt_async(f"▶ {prompt}: ")
        else:
            return input(f"▶ {prompt}: ")

    def display_message(self, msg, level='info'): print(f"[*] {msg}")
    def display_error(self, msg): print(f"[-] ERROR: {msg}")

class MainApp:
    def __init__(self):
        self.root_path = Path(__file__).parent.resolve()
        os.chdir(self.root_path)
        self.view = TerminalView()

    async def run(self):
        self.view.display_banner()
        while True:
            self.view.display_main_menu()
            choice = await self.view.get_user_input("Select option")
            if choice.lower() == '9': break
            elif choice.lower() == '1': self.view.display_message("AI Console not fully implemented in this version.")
            elif choice.lower() == 'n': self.view.display_message("Nuclei scan not fully implemented in this version.")
            else: self.view.display_error("Invalid option.")
        print("\nAlhamdulillah.")

if __name__ == "__main__":
    if sys.version_info < (3, 8):
        print("Requires Python 3.8+")
        sys.exit(1)
    if not PROMPT_TOOLKIT_AVAILABLE:
        print("Core UI dependencies missing. Please run bootstrap again.")
        sys.exit(1)
    app = MainApp()
    try:
        asyncio.run(app.run())
    except KeyboardInterrupt:
        print("\nAlhamdulillah.")