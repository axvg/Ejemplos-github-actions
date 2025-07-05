| Ventaja del deploy automatizado | Riesgo del deploy manual | Contramedida |
| :--- | :--- | :--- |
| Reduce el tiempo de despliegue, permitiendo entregas mas rapidas. | La intervencion manual puede causar errores de configuracion o pasos omitidos. | Implementar scripts de despliegue y usar listas de verificacion para minimizar errores. |
| Cada despliegue sigue el mismo proceso, eliminando variabilidad entre entornos. | Configuraciones manuales pueden causar diferencias entre entornos, generando fallos. | Usar herramientas como Terraform o Ansible para definir infraestructura y asegurar consistencia. |
| Registro claro de que version se desplego, fecha y motivo, facilitando la reversion. | Cambios manuales no documentados dificultan depuracion y rollback. | Versionar scripts de despliegue y registrar acciones en un sistema centralizado. |
