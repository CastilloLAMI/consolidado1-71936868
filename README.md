# Práctica Calificada — Consolidado 1

**Curso:** Construcción de Software (ASUC00947) — VII Ciclo (2026-20)  
**Institución:** Universidad Continental  

---

## Datos del Estudiante
* **Nombre completo:** Iván Ramiro Castillo Mamani
* **Código de alumno:** 71936868
* **Repositorio:** [https://github.com/CastilloLAMI/consolidado1-71936868](https://github.com/CastilloLAMI/consolidado1-71936868)

---

## Descripción del Proyecto
Este proyecto corresponde a la evaluación del Consolidado 1 del curso de Construcción de Software. Implementa soluciones aplicando Programación Orientada a Objetos (POO) en Python (encapsulamiento, propiedades `@property`, herencia y sobreescritura de métodos), siguiendo el flujo de trabajo **Gitflow** y estándares de **Conventional Commits**.

---

## Estructura y Archivos del Repositorio

* **`planeta.py` (Ejercicio 1 — Clase Planeta):**
  * Modela la clase `Planeta` con atributos para nombre, masa (kg), radio (m), distancia al Sol (UA) y presencia de vida.
  * Métodos implementados:
    * `calcular_densidad()`: calcula la densidad media en $kg/m^3$ utilizando la fórmula de volumen esférico $\frac{4}{3}\pi r^3$.
    * `es_planeta_exterior()`: evalúa si la distancia al Sol supera las 5.2 UA.
    * `__str__()`: formato descriptivo con datos y clasificación.
  * Desarrollado en la rama `feature/clase-planeta` e integrado a `develop` mediante `--no-ff`.

* **`automovil.py` (Ejercicio 2 — Clase Automóvil con `@property`):**
  * Modela la clase `Automovil` aplicando encapsulamiento con atributos privados (`_velocidad_max`, `_nivel_combustible`, `_año_fabricacion`).
  * Propiedades `@property` con getters y setters que lanzan `ValueError`:
    * `año_fabricacion`: validado en el rango 1886 a 2026.
    * `nivel_combustible`: validado de 0.0% a 100.0%.
    * `velocidad_max`: validado para valores mayores a 0 km/h.
  * Métodos: `tiempo_llegada(distancia_km)` y `__str__()`.
  * Desarrollado en la rama `feature/clase-automovil` e integrado a `develop` mediante `--no-ff`.

* **`cuentas.py` (Ejercicio 3 — Cuentas Bancarias + Gitflow):**
  * Jerarquía de clases para un sistema financiero:
    * `CuentaBancaria`: Clase base con saldo privado (`__saldo`), métodos de depósito y retiro con validación de montos positivos y saldo suficiente (`ValueError`), y consulta de saldo.
    * `CuentaAhorros`: Hereda de `CuentaBancaria`, incorpora tasa de interés anual y método `calcular_interes()`.
    * `CuentaCorriente`: Hereda de `CuentaBancaria`, añade límite de sobregiro y sobreescribe `retirar()` permitiendo retiro hasta el límite establecido, además de `permite_sobregiro()`.
  * Desarrollado en la rama `feature/cuenta-bancaria`, integrado a `develop`, y aplicado el protocolo de hotfix urgente simulado desde `main`.

* **`README.md`:**
  * Documentación con datos de autoría, detalles de cada módulo y estructura del proyecto.
