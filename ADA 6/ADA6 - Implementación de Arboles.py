import tkinter as tk
from tkinter import messagebox
import random

# ------------------------- CLASES DEL ÁRBOL ------------------------- #
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insertar(self, key):
        if self.root is None:
            self.root = Node(key)
            return True
        curr = self.root
        while True:
            if key == curr.key:
                return False
            elif key < curr.key:
                if curr.left is None:
                    curr.left = Node(key)
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(key)
                    return True
                curr = curr.right

    def buscar(self, key):
        curr = self.root
        while curr:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def eliminar(self, key):
        def _delete_node(node, key):
            if node is None: return None
            if key < node.key:
                node.left = _delete_node(node.left, key)
            elif key > node.key:
                node.right = _delete_node(node.right, key)
            else:
                if node.left is None: return node.right
                if node.right is None: return node.left
                temp = node.right
                while temp.left: temp = temp.left
                node.key = temp.key
                node.right = _delete_node(node.right, temp.key)
            return node
        self.root = _delete_node(self.root, key)

    def eliminar_rama(self, key):
        node = self.buscar(key)
        if node:
            node.left = None
            node.right = None
            return True
        return False

    def eliminar_arbol(self):
        self.root = None


# ------------------------- CANVAS PERSONALIZADO ------------------------- #
class TreeCanvas(tk.Canvas):
    NODE_RADIUS = 30
    LEVEL_HEIGHT = 100

    def __init__(self, parent, bst, **kwargs):
        super().__init__(parent, **kwargs)
        self.bst = bst
        self.width = int(self['width'])
        self.height = int(self['height'])
        self.bind('<Configure>', lambda e: self.redibujar())

    def redibujar(self):
        self.delete('all')
        if self.bst.root:
            self._draw_node(self.bst.root, self.width // 2, 60, self.width // 4)

    def _draw_node(self, node, x, y, x_offset):
        neon_colors = ["#39FF14", "#00FFFF", "#FF10F0", "#FFEA00", "#FF4500"]
        color = random.choice(neon_colors)

        # Líneas más gruesas y coloridas
        if node.left:
            x_left = x - x_offset
            y_child = y + self.LEVEL_HEIGHT
            self.create_line(x, y, x_left, y_child, width=3, fill="#00FFFF")
            self._draw_node(node.left, x_left, y_child, x_offset // 2)
        if node.right:
            x_right = x + x_offset
            y_child = y + self.LEVEL_HEIGHT
            self.create_line(x, y, x_right, y_child, width=3, fill="#FF00FF")
            self._draw_node(node.right, x_right, y_child, x_offset // 2)

        # Nodo con resplandor tipo neón
        self.create_oval(x - self.NODE_RADIUS, y - self.NODE_RADIUS,
                         x + self.NODE_RADIUS, y + self.NODE_RADIUS,
                         fill=color, outline="#111111", width=3)
        self.create_text(x, y, text=str(node.key),
                         font=("Comic Sans MS", 13, "bold"),
                         fill="#000000")


# ------------------------- APLICACIÓN PRINCIPAL ------------------------- #
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🌌 Árbol Binario de Búsqueda - Estilo Neón 🌌")
        self.bst = BST()

        root.configure(bg="#0a0a0a")

        # Marco superior
        control_frame = tk.Frame(root, bg="#1a1a1a", pady=10)
        control_frame.pack(fill=tk.X)

        # Etiqueta
        tk.Label(control_frame, text="Valor:", font=("Consolas", 12, "bold"),
                 bg="#1a1a1a", fg="#00FFFF").pack(side=tk.LEFT, padx=6)
        self.entry = tk.Entry(control_frame, font=("Consolas", 12),
                              width=10, bg="#111111", fg="#39FF14", insertbackground="#39FF14")
        self.entry.pack(side=tk.LEFT, padx=5)

        # Botones rediseñados
        style = dict(font=("Consolas", 11, "bold"), width=13, bd=0, pady=6)
        tk.Button(control_frame, text="➕ Insertar", bg="#39FF14", fg="#000",
                  command=self.insertar, **style).pack(side=tk.LEFT, padx=6)
        tk.Button(control_frame, text="❌ Eliminar Nodo", bg="#FF073A", fg="#fff",
                  command=self.eliminar_nodo, **style).pack(side=tk.LEFT, padx=6)
        tk.Button(control_frame, text="🌿 Eliminar Rama", bg="#FFEA00", fg="#000",
                  command=self.eliminar_rama, **style).pack(side=tk.LEFT, padx=6)
        tk.Button(control_frame, text="🔥 Eliminar Árbol", bg="#00FFFF", fg="#000",
                  command=self.eliminar_arbol, **style).pack(side=tk.LEFT, padx=6)

        # Canvas principal
        self.canvas = TreeCanvas(root, self.bst, width=1000, height=750, bg="#111111", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=10)

    def insertar(self):
        val = self.entry.get().strip()
        if not val:
            return
        try:
            key = int(val)
        except:
            key = val
        self.bst.insertar(key)
        self.entry.delete(0, tk.END)
        self.canvas.redibujar()

    def eliminar_nodo(self):
        val = self.entry.get().strip()
        if not val:
            return
        try:
            key = int(val)
        except:
            key = val
        self.bst.eliminar(key)
        self.entry.delete(0, tk.END)
        self.canvas.redibujar()

    def eliminar_rama(self):
        val = self.entry.get().strip()
        if not val:
            return
        try:
            key = int(val)
        except:
            key = val
        self.bst.eliminar_rama(key)
        self.entry.delete(0, tk.END)
        self.canvas.redibujar()

    def eliminar_arbol(self):
        if messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar todo el árbol?"):
            self.bst.eliminar_arbol()
            self.canvas.redibujar()


# ------------------------- EJECUCIÓN ------------------------- #
def main():
    root = tk.Tk()
    app = App(root)
    root.geometry("1100x800")
    root.mainloop()

if __name__ == "__main__":
    main()
