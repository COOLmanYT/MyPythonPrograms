"""
Modern Scientific Calculator (CustomTkinter)

Requirements:
- Python 3.10+
- customtkinter

What it does:
- Provides a dark-theme calculator UI with responsive grid buttons.
- Supports basic operations (+, -, x, /, %, parentheses, decimal, backspace).
- Includes a toggleable scientific panel (sin, cos, tan, sqrt, log, ln, powers, constants).
- Accepts keyboard input (digits/operators, Enter, Backspace, Escape).
- Uses safe AST-based expression evaluation (no raw eval).

Run:
- python calculator.py
"""

import ast
import math
import operator

import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


ALLOWED_BINOPS = {
	ast.Add: operator.add,
	ast.Sub: operator.sub,
	ast.Mult: operator.mul,
	ast.Div: operator.truediv,
	ast.Pow: operator.pow,
	ast.Mod: operator.mod,
}

ALLOWED_UNARYOPS = {
	ast.UAdd: operator.pos,
	ast.USub: operator.neg,
}

ALLOWED_FUNCS = {
	"sin": math.sin,
	"cos": math.cos,
	"tan": math.tan,
	"sqrt": math.sqrt,
	"log10": math.log10,
	"ln": math.log,
}

ALLOWED_CONSTS = {
	"pi": math.pi,
	"e": math.e,
}


def safe_eval(expression: str) -> float:
	"""Safely evaluate arithmetic and selected scientific functions using AST."""
	node = ast.parse(expression, mode="eval")

	def _eval(n: ast.AST):
		if isinstance(n, ast.Expression):
			return _eval(n.body)

		if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
			return n.value

		if isinstance(n, ast.BinOp) and type(n.op) in ALLOWED_BINOPS:
			left = _eval(n.left)
			right = _eval(n.right)
			return ALLOWED_BINOPS[type(n.op)](left, right)

		if isinstance(n, ast.UnaryOp) and type(n.op) in ALLOWED_UNARYOPS:
			return ALLOWED_UNARYOPS[type(n.op)](_eval(n.operand))

		if isinstance(n, ast.Name) and n.id in ALLOWED_CONSTS:
			return ALLOWED_CONSTS[n.id]

		if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
			fn_name = n.func.id
			if fn_name not in ALLOWED_FUNCS or len(n.args) != 1 or n.keywords:
				raise ValueError("Invalid function call")
			return ALLOWED_FUNCS[fn_name](_eval(n.args[0]))

		raise ValueError("Unsupported expression")

	return _eval(node)


class CalculatorApp(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("Modern Scientific Calculator")
		self.geometry("460x700")
		self.minsize(400, 560)

		self.expression = ""
		self.scientific_mode = False

		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(0, weight=1)

		self._build_ui()
		self._bind_keyboard()

	def _build_ui(self):
		top = ctk.CTkFrame(self, corner_radius=16, fg_color=("#0b1220", "#0b1220"))
		top.grid(row=0, column=0, padx=14, pady=(14, 8), sticky="nsew")
		top.grid_columnconfigure(0, weight=1)

		title = ctk.CTkLabel(
			top,
			text="Calculator",
			font=ctk.CTkFont(size=24, weight="bold"),
		)
		title.grid(row=0, column=0, padx=14, pady=(14, 8), sticky="w")

		self.display_var = ctk.StringVar(value="0")
		self.display = ctk.CTkEntry(
			top,
			textvariable=self.display_var,
			justify="right",
			font=ctk.CTkFont(family="Consolas", size=30),
			height=64,
			corner_radius=12,
		)
		self.display.grid(row=1, column=0, padx=14, pady=(0, 12), sticky="ew")

		self.toggle_btn = ctk.CTkButton(
			top,
			text="Scientific Mode: Off",
			command=self._toggle_scientific,
			height=38,
			corner_radius=10,
			font=ctk.CTkFont(size=14, weight="bold"),
			fg_color="#1d4ed8",
			hover_color="#2563eb",
		)
		self.toggle_btn.grid(row=2, column=0, padx=14, pady=(0, 14), sticky="w")

		body = ctk.CTkFrame(self, corner_radius=16)
		body.grid(row=1, column=0, padx=14, pady=(0, 14), sticky="nsew")
		body.grid_columnconfigure(0, weight=1)
		body.grid_rowconfigure(1, weight=1)

		self.scientific_frame = ctk.CTkFrame(body, fg_color="transparent")
		self.scientific_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
		self.scientific_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
		self._build_scientific_buttons()
		self.scientific_frame.grid_remove()

		self.basic_frame = ctk.CTkFrame(body, fg_color="transparent")
		self.basic_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
		for col in range(4):
			self.basic_frame.grid_columnconfigure(col, weight=1)
		for row in range(5):
			self.basic_frame.grid_rowconfigure(row, weight=1)
		self._build_basic_buttons()

	def _mk_button(self, parent, text, command, row, col, fg, hover):
		btn = ctk.CTkButton(
			parent,
			text=text,
			command=command,
			height=56,
			corner_radius=12,
			font=ctk.CTkFont(size=20, weight="bold"),
			fg_color=fg,
			hover_color=hover,
		)
		btn.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

	def _build_basic_buttons(self):
		layout = [
			["C", "(", ")", "⌫"],
			["7", "8", "9", "÷"],
			["4", "5", "6", "×"],
			["1", "2", "3", "-"],
			["0", ".", "=", "+"],
		]
		for r, row in enumerate(layout):
			for c, text in enumerate(row):
				if text == "C":
					self._mk_button(self.basic_frame, text, self._clear, r, c, "#b91c1c", "#dc2626")
				elif text == "⌫":
					self._mk_button(self.basic_frame, text, self._backspace, r, c, "#475569", "#64748b")
				elif text == "=":
					self._mk_button(self.basic_frame, text, self._evaluate, r, c, "#15803d", "#16a34a")
				elif text in {"+", "-", "×", "÷"}:
					self._mk_button(
						self.basic_frame,
						text,
						lambda t=text: self._append(t),
						r,
						c,
						"#1d4ed8",
						"#2563eb",
					)
				else:
					self._mk_button(
						self.basic_frame,
						text,
						lambda t=text: self._append(t),
						r,
						c,
						"#1f2937",
						"#374151",
					)

	def _build_scientific_buttons(self):
		layout = [
			["sin", "cos", "tan", "sqrt"],
			["log", "ln", "x²", "xʸ"],
			["pi", "e", "%", "±"],
		]
		for r, row in enumerate(layout):
			for c, text in enumerate(row):
				btn = ctk.CTkButton(
					self.scientific_frame,
					text=text,
					command=lambda t=text: self._scientific_action(t),
					height=44,
					corner_radius=10,
					font=ctk.CTkFont(size=16, weight="bold"),
					fg_color="#334155",
					hover_color="#475569",
				)
				btn.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")

	def _bind_keyboard(self):
		self.bind("<Return>", lambda _e: self._evaluate())
		self.bind("<KP_Enter>", lambda _e: self._evaluate())
		self.bind("<BackSpace>", lambda _e: self._backspace())
		self.bind("<Escape>", lambda _e: self._clear())

		for key in "0123456789.+-*/()%":
			self.bind(key, self._on_keypress)

		self.bind("(", self._on_keypress)
		self.bind(")", self._on_keypress)

	def _on_keypress(self, event):
		char = event.char
		if not char:
			return
		if char == "*":
			self._append("×")
		elif char == "/":
			self._append("÷")
		else:
			self._append(char)

	def _toggle_scientific(self):
		self.scientific_mode = not self.scientific_mode
		if self.scientific_mode:
			self.scientific_frame.grid()
			self.toggle_btn.configure(text="Scientific Mode: On")
		else:
			self.scientific_frame.grid_remove()
			self.toggle_btn.configure(text="Scientific Mode: Off")

	def _append(self, token: str):
		self.expression += token
		self.display_var.set(self.expression or "0")

	def _clear(self):
		self.expression = ""
		self.display_var.set("0")

	def _backspace(self):
		self.expression = self.expression[:-1]
		self.display_var.set(self.expression or "0")

	def _scientific_action(self, action: str):
		if action in {"sin", "cos", "tan", "sqrt", "ln"}:
			self._append(f"{action}(")
			return
		if action == "log":
			self._append("log10(")
			return
		if action == "x²":
			self._append("**2")
			return
		if action == "xʸ":
			self._append("**")
			return
		if action == "%":
			self._append("%")
			return
		if action == "±":
			self.expression = f"(-({self.expression}))" if self.expression else "-"
			self.display_var.set(self.expression)
			return

		self._append(action)

	def _evaluate(self):
		if not self.expression:
			return

		safe_expr = self.expression.replace("×", "*").replace("÷", "/")
		try:
			result = safe_eval(safe_expr)
			if isinstance(result, float) and result.is_integer():
				result = int(result)
			self.expression = str(result)
			self.display_var.set(self.expression)
		except Exception:
			self.expression = ""
			self.display_var.set("Error")


if __name__ == "__main__":
	app = CalculatorApp()
	app.mainloop()
