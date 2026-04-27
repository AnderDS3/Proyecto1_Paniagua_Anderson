# proyecto1_Paniagua_Anderson

Calculadora de fracciones con interfaz gráfica, desarrollada en Python usando el patrón MVC.

---

## ¿Qué hace?

Permite al usuario ingresar fracciones y realizar las siguientes operaciones:

- Sumar, restar, multiplicar y dividir todas las fracciones ingresadas
- Encontrar la fracción mayor y la menor
- Ordenar las fracciones de mayor a menor
- Simplificar fracciones automáticamente
- Limpiar la lista de fracciones

---

## Estructura del proyecto

```
proyecto1_Paniagua_Anderson/
├── README.md
├── requirements.txt
├── datos/
│   └── fracciones.json
├── src/
│   ├── main.py
│   ├── models/
│   │   └── model.py
│   ├── views/
│   │   └── view.py
│   └── controllers/
│       └── controller.py
└── tests/
    └── test_fracciones.py
```

---

## Requisitos

No requiere librerías externas. Solo necesitas tener **Python 3** instalado.

---

## ¿Cómo ejecutar?

Desde la carpeta raíz del proyecto, corre:

```bash ejecutar:
python src/main.py
```

---

## ¿Cómo correr los tests?

Desde la carpeta raíz del proyecto, corre:

```bash ejecutar:
python -m unittest discover tests
```

---

## Autor

Dany Paniagua
