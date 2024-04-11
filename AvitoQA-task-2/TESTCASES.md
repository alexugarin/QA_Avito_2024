### Классы эквивалентности и граничные значения
Эквивалентные классы и их граничные значения для каждого счетчика:

<table>
<thead>
		<tr>
			<td><strong>N Тест-кейса</strong></td>
			<td><strong>Единица измерения счетчика сохраненного объема воды</strong></td>
			<td><strong>Единица измерения счетчика предотвращённого объёма выброса CO2</strong></td>
			<td><strong>Единица измерения счетчика сэкономленной электроэнергии</strong></td>
			<td><strong>Граничное значение | Полученное с бэкенда значение</strong></td>
			<td><strong>Ожидаемое значение | Отображаемое значение счетчика</strong></td>
		</tr>
</thead>
	<tbody>
		<tr>
			<td>1.1</td>
			<td rowspan="4">л  </td>
			<td rowspan="4">кг </td>
			<td rowspan="4">кВт⋅ч </td>
			<td>-1</td>
			<td>0 / Не должно отобразиться</td>
		</tr>
		<tr>
			<td>1.2</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1.3</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1.4</td>
			<td>999</td>
			<td>999</td>
		</tr>
		<tr>
			<td>2.1</td>
			<td rowspan="4">м³ </td>
			<td rowspan="4">тонн</td>
			<td rowspan="4">МВт⋅ч</td>
			<td>1 000</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2.2</td>
			<td>1 001</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2.3</td>
			<td>1 100</td>
			<td>1.1</td>
		</tr>
		<tr>
			<td>2.4</td>
			<td>999 999</td>
			<td>999.9</td>
		</tr>
		<tr>
			<td>3.1</td>
			<td rowspan="3">тыс м³</td>
			<td rowspan="3">млн кг</td>
			<td rowspan="3">млн кВт⋅ч</td>
			<td>1 000 000</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3.2</td>
			<td>1 100 000</td>
			<td>1.1</td>
		</tr>
		<tr>
			<td>3.3</td>
			<td>999 999 999</td>
			<td>999.9</td>
		</tr>
		<tr>
			<td>4.1</td>
			<td rowspan="3">млн м³ </td>
			<td rowspan="3">млн тонн</td>
			<td rowspan="3">млн МВт⋅ч</td>
			<td>1 000 000 000</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4.2</td>
			<td>1 100 000 000</td>
			<td>1.1</td>
		</tr>
		<tr>
			<td>4.3</td>
			<td>999 999 999 999</td>
			<td>999.9</td>
		</tr>
		<tr>
			<td>5.1</td>
			<td rowspan="4">млрд м³</td>
			<td rowspan="4">млрд тонн</td>
			<td rowspan="4">млрд МВт⋅ч</td>
			<td>1 000 000 000 000</td>
			<td>1</td>
		</tr>
		<tr>
			<td>5.2</td>
			<td>1 100 000 000 000</td>
			<td>1.1</td>
		</tr>
		<tr>
			<td>5.3</td>
			<td>999 999 999 999 999</td>
			<td>999.9</td>
		</tr>
		<tr>
			<td>5.4</td>
			<td>9 999 999 999 999 999</td>
			<td>9 999.9 / Не должно отобразиться</td>
		</tr>
	</tbody>
</table>
