import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. Account(계좌) 클래스 : 데이터 및 핵심 로직 담당
# ==========================================
class Account:
    def __init__(self, owner, pin, balance=500000):
        """
        계좌 초기화 함수
        - owner: 예금주 이름
        - pin: 비밀번호 (4자리 문자열)
        - balance: 초기 잔액 (기본값 500,000원)
        """
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.login_attempts = 0  # 비밀번호 오류 횟수 카운트

    def check_pin(self, entered_pin):
        """ 비밀번호 인증 및 보안 처리 """
        if self.pin == entered_pin:
            self.login_attempts = 0  # 인증 성공 시 실패 횟수 초기화
            return True
        else:
            self.login_attempts += 1
            return False

    def deposit(self, amount):
        """ 입금 기능 (데이터 무결성 검증) """
        if amount <= 0:
            return False, "올바른 금액을 입력해주세요."
        
        self.balance += amount
        return True, f"{amount:,}원이 입금되었습니다."

    def withdraw(self, amount):
        """ 출금 기능 (잔액 부족 예외 처리) """
        if amount <= 0:
            return False, "올바른 금액을 입력해주세요."
        if amount > self.balance:
            return False, "잔액이 부족합니다."
        
        self.balance -= amount
        return True, f"{amount:,}원이 출금되었습니다."


# ==========================================
# 2. ATMApp 클래스 : 사용자 화면(GUI) 및 이벤트 제어
# ==========================================
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("소프트웨어학과 ATM 시스템")
        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e2e") # 개발자 친화적인 다크 폰트 배경

        # 테스트용 샘플 계좌 데이터 생성 (예금주: 김민준, PIN: 1234)
        self.account = Account(owner="김민준", pin="1234", balance=500000)

        # 프로그램 시작 시 로그인 화면 띄우기
        self.show_login_screen()

    def clear_window(self):
        """ 화면 전환을 위해 기존 위젯들을 모두 지우는 함수 """
        for widget in self.root.winfo_children():
            widget.destroy()

    # ------------------------------------------
    # [화면 1] 로그인 화면 구현
    # ------------------------------------------
    def show_login_screen(self):
        self.clear_window()

        # 타이틀
        title = tk.Label(self.root, text="🏪 OOP BANK ATM", font=("Helvetica", 20, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        title.pack(pady=50)

        # 안내 메시지
        lbl_info = tk.Label(self.root, text="비밀번호 4자리를 입력하세요.", font=("Malgun Gothic", 11), fg="#a6adc8", bg="#1e1e2e")
        lbl_info.pack(pady=10)

        # 비밀번호 입력창 (입력 시 *로 표시)
        self.entry_pin = tk.Entry(self.root, font=("Helvetica", 16), show="*", justify="center", width=12, bg="#313244", fg="#cdd6f4", bd=0)
        self.entry_pin.pack(pady=10)
        self.entry_pin.focus()

        # 로그인 버튼
        btn_login = tk.Button(self.root, text="인증하기", font=("Malgun Gothic", 12, "bold"), bg="#a6e3a1", fg="#11111b", width=12, command=self.handle_login, relief="flat")
        btn_login.pack(pady=20)

    def handle_login(self):
        """ 로그인 인증 버튼 클릭 이벤트 처리 """
        entered_pin = self.entry_pin.get()
        
        if self.account.check_pin(entered_pin):
            messagebox.showinfo("인증 성공", f"어서오세요, {self.account.owner}님!")
            self.show_main_screen()
        else:
            if self.account.login_attempts >= 3:
                messagebox.showerror("보안 경고", "비밀번호 3회 이상 오류로 프로그램을 강제 종료합니다.")
                self.root.quit()
            else:
                messagebox.showwarning("인증 실패", f"비밀번호가 틀렸습니다.\n(오류 횟수: {self.account.login_attempts}/3)")

    # ------------------------------------------
    # [화면 2] 메인 거래 화면 구현
    # ------------------------------------------
    def show_main_screen(self):
        self.clear_window()

        # 상단 사용자 정보 바
        user_info = tk.Label(self.root, text=f"👤 사용자: {self.account.owner}", font=("Malgun Gothic", 11, "bold"), fg="#cdd6f4", bg="#313244", width=40, pady=8)
        user_info.pack(pady=15)

        # 실시간 잔액 표시 레이블
        self.lbl_balance = tk.Label(self.root, text=f"현재 잔액: {self.account.balance:,} 원", font=("Malgun Gothic", 16, "bold"), fg="#f9e2af", bg="#1e1e2e")
        self.lbl_balance.pack(pady=20)

        # 금액 입력 프레임
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(pady=15)

        tk.Label(input_frame, text="금액 입력: ", font=("Malgun Gothic", 12), fg="#cdd6f4", bg="#1e1e2e").grid(row=0, column=0)
        self.entry_amount = tk.Entry(input_frame, font=("Helvetica", 14), width=12, bg="#313244", fg="#cdd6f4", bd=0)
        self.entry_amount.grid(row=0, column=1, padx=5)
        tk.Label(input_frame, text="원", font=("Malgun Gothic", 12), fg="#cdd6f4", bg="#1e1e2e").grid(row=0, column=2)

        # 기능 버튼 프레임
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(pady=25)

        tk.Button(btn_frame, text="💰 입금하기", font=("Malgun Gothic", 11, "bold"), bg="#89b4fa", fg="#11111b", width=12, height=2, command=self.handle_deposit, relief="flat").grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="💸 출금하기", font=("Malgun Gothic", 11, "bold"), bg="#f38ba8", fg="#11111b", width=12, height=2, command=self.handle_withdraw, relief="flat").grid(row=0, column=1, padx=10)
        
        # 로그아웃 버튼
        tk.Button(self.root, text="↩ 안전하게 로그아웃", font=("Malgun Gothic", 10), bg="#45475a", fg="#cdd6f4", width=20, command=self.show_login_screen, relief="flat").pack(pady=20)

    def handle_deposit(self):
        """ 입금 버튼 클릭 시 예외 처리 및 반영 """
        try:
            amount = int(self.entry_amount.get()) # 입력값을 숫자로 변환 (ValueError 발생 가능 구역)
            success, msg = self.account.deposit(amount)
            if success:
                messagebox.showinfo("입금 성공", msg)
                self.update_balance_display()
            else:
                messagebox.showwarning("입금 제한", msg)
        except ValueError:
            messagebox.showerror("입력 오류", "숫자만 정확하게 입력해주세요.")
        finally:
            self.entry_amount.delete(0, tk.END)

    def handle_withdraw(self):
        """ 출금 버튼 클릭 시 예외 처리 및 반영 """
        try:
            amount = int(self.entry_amount.get())
            success, msg = self.account.withdraw(amount)
            if success:
                messagebox.showinfo("출금 성공", msg)
                self.update_balance_display()
            else:
                messagebox.showwarning("출금 제한", msg)
        except ValueError:
            messagebox.showerror("입력 오류", "숫자만 정확하게 입력해주세요.")
        finally:
            self.entry_amount.delete(0, tk.END)

    def update_balance_display(self):
        """ 실시간 잔액 새로고침 함수 """
        self.lbl_balance.config(text=f"현재 잔액: {self.account.balance:,} 원")


# ==========================================
# 3. 프로그램 시작점
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()