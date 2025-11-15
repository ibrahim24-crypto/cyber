from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import sys
import subprocess

# ANSI Color codes for styling
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Hacker mode colors
    HACKER_GREEN = '\033[38;5;46m'
    HACKER_LIME = '\033[38;5;118m'
    HACKER_DARK = '\033[38;5;22m'

def print_banner_normal():
    """Print normal mode banner"""
    print(f"{Colors.OKBLUE}{Colors.BOLD}")
    print("╔════════════════════════════════════════╗")
    print("║     Router Reboot Automation v2.0      ║")
    print("║          Normal Mode Active            ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")

def print_banner_hacker():
    """Print hacker mode banner"""
    print(f"{Colors.HACKER_GREEN}{Colors.BOLD}")
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃   ██████╗  ██████╗ ██╗   ██╗████████╗ ┃")
    print("┃   ██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝ ┃")
    print("┃   ██████╔╝██║   ██║██║   ██║   ██║    ┃")
    print("┃   ██╔══██╗██║   ██║██║   ██║   ██║    ┃")
    print("┃   ██║  ██║╚██████╔╝╚██████╔╝   ██║    ┃")
    print("┃   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝    ┃")
    print("┃                                        ┃")
    print("┃      REBOOT AUTOMATION SYSTEM          ┃")
    print("┃         [ HACKER MODE ]                ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(f"{Colors.ENDC}")

def log_normal(step, total, message, status="info"):
    """Log message in normal mode"""
    if status == "success":
        icon = "✓"
        color = Colors.OKGREEN
    elif status == "error":
        icon = "✗"
        color = Colors.FAIL
    elif status == "warning":
        icon = "⚠"
        color = Colors.WARNING
    else:
        icon = "►"
        color = Colors.OKCYAN
    
    print(f"{color}[{step}/{total}] {icon} {message}{Colors.ENDC}")

def log_hacker(message, level="info"):
    """Log message in hacker mode"""
    timestamp = time.strftime("%H:%M:%S")
    
    if level == "success":
        prefix = "[+]"
        color = Colors.HACKER_GREEN
    elif level == "error":
        prefix = "[!]"
        color = Colors.FAIL
    elif level == "warning":
        prefix = "[*]"
        color = Colors.WARNING
    elif level == "progress":
        prefix = "[~]"
        color = Colors.HACKER_LIME
    else:
        prefix = "[>]"
        color = Colors.HACKER_DARK
    
    print(f"{color}{timestamp} {prefix} {message}{Colors.ENDC}")

def wait_for_page_load(driver, timeout=15):
    """Wait for page to be fully loaded"""
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        return True
    except TimeoutException:
        return False

def automate_tenda_router(mode="normal"):
    """Main automation function"""
    is_hacker = (mode == "hacker")
    
    # Print banner
    if is_hacker:
        print_banner_hacker()
        log_hacker("Initializing router exploitation sequence...", "info")
        log_hacker("Target: Tenda Router @ 192.168.1.1", "info")
    else:
        print_banner_normal()
        log_normal(0, 5, "Initializing automation...", "info")
    
    # Set up Brave browser options for Linux
    opts = webdriver.ChromeOptions()
    opts.binary_location = "/usr/bin/brave-browser"
    opts.add_argument("--start-maximized")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    
    if is_hacker:
        log_hacker("Configuring stealth browser parameters...", "progress")
    
    driver_path = "/home/ibrahim/drivers/brave/chromedriver"
    service = Service(driver_path)
    
    try:
        driver = webdriver.Chrome(service=service, options=opts)
        driver.implicitly_wait(3)
        wait = WebDriverWait(driver, 15)
        
        if is_hacker:
            log_hacker("Browser instance spawned successfully", "success")
        
        # Step 1: Login
        if is_hacker:
            log_hacker("Establishing connection to target...", "progress")
        else:
            log_normal(1, 5, "Opening router login page...", "info")
        
        driver.get("http://192.168.1.1/login.html")
        wait_for_page_load(driver, timeout=10)
        
        try:
            username_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
            password_field = driver.find_element(By.ID, "login-password")
            login_button = driver.find_element(By.ID, "submit")
            
            if is_hacker:
                log_hacker("Login portal detected", "info")
                log_hacker("Injecting credentials...", "progress")
            
            username_field.clear()
            username_field.send_keys("admin")
            password_field.clear()
            password_field.send_keys("08628791")
            login_button.click()
            
            if is_hacker:
                log_hacker("Authentication payload delivered", "success")
            else:
                log_normal(1, 5, "Login credentials submitted", "success")
        except Exception as e:
            if is_hacker:
                log_hacker(f"Authentication failed: {str(e)}", "error")
            else:
                log_normal(1, 5, f"Login failed: {str(e)}", "error")
            return 1
        
        # Wait for login
        time.sleep(2)
        wait_for_page_load(driver, timeout=8)
        
        # Verify login
        for i in range(5):
            if "index.html" in driver.current_url:
                if is_hacker:
                    log_hacker("Access granted - Infiltration successful", "success")
                else:
                    log_normal(1, 5, "Login successful", "success")
                break
            elif i < 4:
                time.sleep(1)
        
        # Step 2: Access Advanced Settings
        if is_hacker:
            log_hacker("Navigating to advanced control panel...", "progress")
        else:
            log_normal(2, 5, "Accessing Advanced settings...", "info")
        
        time.sleep(1)
        
        try:
            advanced_button = wait.until(EC.element_to_be_clickable((By.ID, "advset")))
            driver.execute_script("arguments[0].click();", advanced_button)
            
            if is_hacker:
                log_hacker("Advanced settings module accessed", "success")
            else:
                log_normal(2, 5, "Advanced settings opened", "success")
        except:
            if is_hacker:
                log_hacker("Failed to access advanced controls", "error")
            else:
                log_normal(2, 5, "Could not access Advanced settings", "error")
            return 1
        
        time.sleep(1)
        wait_for_page_load(driver, timeout=8)
        
        # Step 3: Navigate to Management > Reboot
        if is_hacker:
            log_hacker("Scanning for system management interface...", "progress")
        else:
            log_normal(3, 5, "Navigating to Reboot section...", "info")
        
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it("menufrm"))
            if is_hacker:
                log_hacker("Menu frame injection successful", "info")
        except:
            if is_hacker:
                log_hacker("Menu frame injection failed", "error")
            else:
                log_normal(3, 5, "Could not access menu frame", "error")
            return 1
        
        try:
            management_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Management')]")))
            driver.execute_script("arguments[0].click();", management_tab)
            
            if is_hacker:
                log_hacker("Management module located", "info")
            
            time.sleep(0.5)  # Reduced wait time
            
            reboot_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Reboot')]")))
            driver.execute_script("arguments[0].click();", reboot_option)
            
            if is_hacker:
                log_hacker("Reboot function isolated", "success")
            else:
                log_normal(3, 5, "Reboot option selected", "success")
        except Exception as e:
            if is_hacker:
                log_hacker(f"Navigation error: {str(e)}", "error")
            else:
                log_normal(3, 5, f"Navigation failed: {str(e)}", "error")
            return 1
        
        time.sleep(0.5)  # Reduced wait time
        
        # Step 4: Execute Reboot
        if is_hacker:
            log_hacker("Preparing reboot sequence...", "progress")
        else:
            log_normal(4, 5, "Initiating router reboot...", "info")
        
        driver.switch_to.default_content()
        
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it("basefrm"))
            if is_hacker:
                log_hacker("Base frame accessed", "info")
        except:
            if is_hacker:
                log_hacker("Base frame access denied", "error")
            else:
                log_normal(4, 5, "Could not access reboot page", "error")
            return 1
        
        try:
            reboot_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Reboot']")))
            driver.execute_script("arguments[0].click();", reboot_button)
            
            if is_hacker:
                log_hacker("Reboot command injected", "success")
            else:
                log_normal(4, 5, "Reboot button clicked", "success")
        except Exception as e:
            if is_hacker:
                log_hacker(f"Reboot execution failed: {str(e)}", "error")
            else:
                log_normal(4, 5, f"Could not click reboot button: {str(e)}", "error")
            return 1
        
        # Handle confirmation alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            
            if is_hacker:
                log_hacker("Confirmation bypass executed", "success")
            else:
                log_normal(4, 5, "Reboot confirmed", "success")
        except:
            if is_hacker:
                log_hacker("No confirmation required", "info")
        
        # Step 5: Monitor for internet loss
        if is_hacker:
            log_hacker("Reboot sequence initiated successfully", "success")
            log_hacker("Monitoring network connectivity...", "progress")
        else:
            log_normal(5, 5, "Monitoring for internet loss...", "info")
        
        driver.switch_to.default_content()
        
        if is_hacker:
            log_hacker("Pinging external hosts to detect outage...", "info")
        
        internet_lost = False
        attempt = 0
        while not internet_lost:
            attempt += 1
            try:
                result = subprocess.run(
                    ['ping', '-c', '1', '-W', '1', '8.8.8.8'],
                    capture_output=True,
                    timeout=2
                )
                
                if result.returncode != 0:
                    internet_lost = True
                    if is_hacker:
                        log_hacker(f"Network outage detected after {attempt}s", "success")
                        log_hacker("Router reboot confirmed - Target is offline", "success")
                    else:
                        log_normal(5, 5, f"Internet lost detected at {attempt}s", "success")
                    break
                
                if attempt % 5 == 0:
                    if is_hacker:
                        log_hacker(f"Network still active... ({attempt}s elapsed)", "progress")
                    else:
                        print(f"{Colors.OKCYAN}    Waiting... ({attempt}s){Colors.ENDC}")
                
                time.sleep(1)
                
            except subprocess.TimeoutExpired:
                internet_lost = True
                if is_hacker:
                    log_hacker(f"Network timeout detected after {attempt}s", "success")
                    log_hacker("Router reboot confirmed - Target is offline", "success")
                else:
                    log_normal(5, 5, f"Internet lost detected at {attempt}s", "success")
                break
            except Exception as e:
                internet_lost = True
                if is_hacker:
                    log_hacker(f"Network failure detected after {attempt}s", "success")
                    log_hacker("Router reboot confirmed - Target is offline", "success")
                else:
                    log_normal(5, 5, f"Internet lost detected at {attempt}s", "success")
                break
        
        # Success
        if is_hacker:
            print(f"\n{Colors.HACKER_GREEN}{Colors.BOLD}")
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃    MISSION ACCOMPLISHED                ┃")
            print("┃    Router reboot executed successfully┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print(f"{Colors.ENDC}")
            log_hacker("Closing connection...", "info")
        else:
            print(f"\n{Colors.OKGREEN}{Colors.BOLD}")
            print("╔════════════════════════════════════════╗")
            print("║   ✓ Router Reboot Completed!           ║")
            print("╚════════════════════════════════════════╝")
            print(f"{Colors.ENDC}")
        
        return 0
        
    except Exception as e:
        if is_hacker:
            log_hacker(f"CRITICAL ERROR: {str(e)}", "error")
        else:
            log_normal(0, 5, f"Script failed: {str(e)}", "error")
        import traceback
        traceback.print_exc()
        return 1
        
    finally:
        if is_hacker:
            log_hacker("Cleaning up traces...", "info")
        else:
            print(f"\n{Colors.OKCYAN}Cleaning up...{Colors.ENDC}")
        try:
            driver.quit()
            if is_hacker:
                log_hacker("Browser instance terminated", "success")
        except:
            pass

def show_mode_selection():
    """Show mode selection menu"""
    print(f"{Colors.BOLD}{Colors.OKCYAN}")
    print("\n╔════════════════════════════════════════╗")
    print("║   Router Reboot Automation Script     ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.ENDC}")
    print(f"\n{Colors.BOLD}Select Mode:{Colors.ENDC}")
    print(f"{Colors.OKBLUE}[1]{Colors.ENDC} Normal Mode  - Clean and simple interface")
    print(f"{Colors.HACKER_GREEN}[2]{Colors.ENDC} Hacker Mode - Matrix-style terminal output")
    print(f"{Colors.WARNING}[0]{Colors.ENDC} Exit")
    
    while True:
        try:
            choice = input(f"\n{Colors.BOLD}Enter your choice (1/2/0): {Colors.ENDC}").strip()
            if choice == "1":
                return "normal"
            elif choice == "2":
                return "hacker"
            elif choice == "0":
                print(f"{Colors.WARNING}Exiting...{Colors.ENDC}")
                sys.exit(0)
            else:
                print(f"{Colors.FAIL}Invalid choice. Please enter 1, 2, or 0.{Colors.ENDC}")
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Interrupted by user{Colors.ENDC}")
            sys.exit(0)

if __name__ == "__main__":
    mode = show_mode_selection()
    print("\n")
    exit_code = automate_tenda_router(mode)
    print(f"\n{Colors.OKCYAN}Exit code: {exit_code}{Colors.ENDC}")
    sys.exit(exit_code)
