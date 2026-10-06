from pathlib import Path
import json
from decimal import Decimal

data = json.loads(Path(__file__).with_name('scenario.json').read_text(encoding='utf-8'))
assert data['synthetic'] is True
assert Decimal(str(data['approved_liters'])) - Decimal(str(data['dispatch_liters'])) == Decimal(str(data['remaining_liters']))
assert data['exact_retry_additional_liters'] == 0
assert data['unit'].startswith('DEMO-')
print('Comprobación de coherencia de escenario sintético: saldo aritmético y valor esperado de descuento adicional.')
print('Este ejemplo no ejecuta solicitudes repetidas ni valida el mecanismo operativo de idempotencia.')
print(f"Unidad: {data['unit']} | Cuota aprobada: {data['approved_liters']} L | Despachado: {data['dispatch_liters']} L | Saldo: {data['remaining_liters']} L")
print(f"Reintento con misma clave: +{data['exact_retry_additional_liters']} L adicionales esperados (coherencia de escenario sintético)")
