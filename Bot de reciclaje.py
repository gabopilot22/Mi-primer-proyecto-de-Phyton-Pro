import random
import discord
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='¡', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, mi nombre es BOT DE RECICLAJE y estoy aqui para ayudarte: a continuacion te voy a dar la lista de comandos seguidos del signo (¡) puedes utilizar para ayudarte: 1. como reducir la contaminacion ambiental  2. como se clasifican los residuos y a cual pertenece cada uno  3. como compartir el mensaje para evitar la contaminacion ambiental     4. en cuanto tiempo se desintegra el papel  5. como puedo empezar a aprovechar mis residuos de una manera eficiente 6. errores al momento de reciclar   7. como ha afectado la contaminacion ambiental con el desarrolo del medio ambiente y porque {bot.user}!')

@bot.command()
async def como_reducir_la_contaminacion_ambiental(ctx):
    await ctx.send(f'Transporte Sostenible y Energía Limpia: Usa transporte público, bicicletas o vehículos eléctricos, y fomenta el uso de energías renovables como solar y eólica. Eficiencia Energética: Utiliza electrodomésticos eficientes y mejora el aislamiento en edificios para reducir el consumo de energía. Gestión de Residuos: Recicla y compostaje de residuos, y reduce el uso de productos desechables. Conservación de Recursos Naturales: Ahorra agua y apoya la protección de ecosistemas naturales. Políticas Públicas: Promueve y apoya leyes que regulen la contaminación y fomenten prácticas sostenibles. Educación y Conciencia: Educa a otros sobre los impactos ambientales y participa en iniciativas locales para el medio ambiente. Innovación Tecnológica: Apoya el desarrollo de tecnologías limpias y el monitoreo ambiental para una mejor gestión de recursos. Implementando estas acciones en conjunto, puedes contribuir significativamente a reducir la contaminación ambiental.{bot.user}!') 


@bot.command()
async def como_se_clasifican_los_residuos(ctx):
    await ctx.send(f'La clasificación de los residuos es un proceso importante para su correcta gestión y reciclaje. Aquí tienes una descripción de las principales categorías:
                    1. Residuos Orgánicos
                    Descripción: Son aquellos residuos de origen biológico que se descomponen de manera natural. Incluyen restos de comida, cáscaras de frutas y verduras, hojas, césped, flores y otros residuos de jardín.
                    Destino: Pueden convertirse en compost o abono orgánico mediante procesos de descomposición.
                    2. Residuos Inorgánicos Reciclables
                    Descripción: Materiales que pueden ser reintroducidos en el ciclo productivo tras su reciclaje.
                    Papel y cartón: Periódicos, revistas, cajas de cartón, folletos.
                    Plásticos: Botellas, envases, bolsas, productos de plástico duro.
                    Vidrio: Botellas, frascos, envases de vidrio.
                    Metales: Latas de aluminio, acero, productos de hojalata.
                    Destino: Se deben separar según el tipo de material y llevar a los centros de reciclaje o contenedores específicos.
                    3. Residuos Inorgánicos No Reciclables
                    Descripción: Residuos que no pueden ser reciclados debido a su composición o contaminación.
                    Ejemplos: Papel higiénico, pañales, colillas de cigarrillos, algunos tipos de envoltorios.
                    Destino: Estos residuos suelen ser enviados a vertederos o incineradoras.
                    4. Residuos Peligrosos
                    Descripción: Son residuos que pueden ser dañinos para la salud humana y el medio ambiente si no se manejan correctamente.
                    Ejemplos: Baterías, pilas, productos químicos, medicamentos caducados, residuos electrónicos, pinturas, solventes.
                    Destino: Deben ser manejados de manera especial, a través de puntos de recogida específicos o campañas de recolección.
                    5. Residuos Sanitarios
                    Descripción: Residuos generados en actividades de atención médica y sanitaria.
                    Ejemplos: Jeringas, gasas, guantes, material de curación.
                    Destino: Deben ser gestionados con estrictas medidas de seguridad para evitar riesgos biológicos.
                    6. Residuos Voluminosos
                    Descripción: Residuos de gran tamaño que no pueden ser recogidos con los residuos domésticos habituales.
                    Ejemplos: Muebles, electrodomésticos, colchones.
                    Destino: Se suelen llevar a puntos limpios o centros de reciclaje específicos.
                    7. Residuos de Construcción y Demolición
                    Descripción: Materiales generados en obras de construcción, remodelación, o demolición.
                    Ejemplos: Escombros, ladrillos, cemento, madera.
                    Destino: Se deben llevar a centros de reciclaje especializados en este tipo de residuos.
                    8. Residuos Especiales
                    Descripción: Residuos que requieren un manejo particular debido a su naturaleza.
                    Ejemplos: Aceites usados, neumáticos, lámparas fluorescentes.
                    Destino: Deben ser gestionados a través de servicios de recogida especiales o puntos limpios.
                    Cada tipo de residuo requiere un manejo específico para minimizar su impacto ambiental y aprovechar al máximo los recursos que contienen. {bot.user}!')

@bot.command()
async def como_compartir_el_mensaje_para_evitar_la_contaminacion_ambiental(ctx):
    await ctx.send(f'Compartir un mensaje efectivo para evitar la contaminación ambiental requiere claridad, concisión y un enfoque en acciones concretas que las personas puedan tomar. Aquí tienes algunas estrategias y ejemplos de cómo comunicar este mensaje:
                        ### 1. **Utiliza Mensajes Claros y Directos**
                        - **Ejemplo**: "Recicla y reduce los desechos: ¡Tu pequeña acción cuenta para un gran cambio!"
                        ### 2. **Enfócate en Acciones Específicas**
                        - **Ejemplo**: "Evita usar plásticos de un solo uso: Lleva tu propia bolsa y botella reutilizable."
                        ### 3. **Incorpora Datos Impactantes**
                        - **Ejemplo**: "Cada año, 8 millones de toneladas de plástico llegan a los océanos. ¡Reduce tu consumo de plástico ahora!"
                        ### 4. **Apela a las Emociones**
                        - **Ejemplo**: "Protejamos la Tierra para las futuras generaciones: Cada acción cuenta."
                        ### 5. **Promueve la Educación Ambiental**
                        - **Ejemplo**: "Infórmate sobre cómo reciclar correctamente en tu comunidad. ¡Haz la diferencia!"
                        ### 6. **Fomenta la Responsabilidad Personal**
                        - **Ejemplo**: "El cambio empieza contigo: ¡Cuida el planeta con pequeñas acciones diarias!"
                        ### 7. **Usa Imágenes y Visuales**
                        - Combina tu mensaje con imágenes impactantes que muestren las consecuencias de la contaminación y los beneficios de la conservación.
                        ### 8. **Hazlo Viral en Redes Sociales**
                        - Utiliza hashtags como #CuidaElPlaneta, #MenosPlástico, #Recicla, y comparte consejos, infografías y videos que puedan ser fácilmente compartidos por otros.
                        ### 9. **Organiza Campañas o Eventos Comunitarios**
                        - Invita a la comunidad a participar en actividades como limpieza de playas, talleres de reciclaje, o charlas sobre sostenibilidad.
                        ### 10. **Muestra el Impacto Positivo de las Acciones**
                        - **Ejemplo**: "Por cada tonelada de papel reciclado, se salvan 17 árboles. ¡Tu esfuerzo cuenta!"
                        ### 11. **Colabora con Organizaciones y Movimientos**
                        - Alía tu mensaje con grupos ecológicos locales o internacionales para amplificar el alcance.
                        ### 12. **Utiliza Testimonios o Casos de Éxito**
                        - Muestra ejemplos de cómo las personas o comunidades han reducido su huella ambiental y los beneficios que han logrado.
                        ### 13. **Mantén un Mensaje Positivo**
                        - **Ejemplo**: "Juntos, podemos crear un futuro más limpio y verde para todos."
                        ### Ejemplo de Mensaje Integral:
                        **"Reduce, reutiliza, recicla. Cada pequeño esfuerzo cuenta: Lleva tu propia botella, evita el plástico de un solo uso, y separa tus residuos. Protejamos juntos el medio ambiente para las futuras generaciones. ¡El cambio empieza contigo!"**
                        Este enfoque asegura que el mensaje sea claro, impactante y fácil de seguir, motivando a las personas a tomar medidas para evitar la contaminación ambiental.{bot.user}!')


@bot.command()
async def en_cuanto_tiempo_se_desintegra_el_papel(ctx):
    await ctx.send(f'El tiempo que tarda en desintegrarse el papel depende de varios factores, como el tipo de papel, las condiciones ambientales (como la humedad y la exposición al sol) y si el papel está enterrado o expuesto al aire libre. Sin embargo, en promedio:
                    - **Papel normal (como el de oficina o periódico):** Puede tardar entre **2 a 5 meses** en desintegrarse completamente cuando está expuesto a condiciones ambientales normales.
                    
                    - **Papel tratado o con recubrimiento (como papel encerado o con plastificado):** Puede tardar más tiempo en descomponerse, en algunos casos hasta **6 meses o más**.
                    Es importante señalar que el papel es biodegradable y, bajo las condiciones adecuadas (como en un proceso de compostaje), puede descomponerse incluso más rápido. Sin embargo, si se dispone incorrectamente, como en un vertedero donde no hay suficiente oxígeno, el papel puede tardar más tiempo en desintegrarse.{bot.user}!')

@bot.command()
async def como_puedo_aprovechar_mis_residuos_eficientemente(ctx):
    await ctx.send(f'Aprovechar eficientemente tus residuos es una excelente manera de reducir el impacto ambiental y promover la sostenibilidad. Aquí te dejo algunas estrategias y consejos para hacerlo:
                    ### 1. **Reciclaje**
                    - **Clasificación correcta:** Separa los residuos reciclables (papel, cartón, vidrio, plástico, metales) y llévalos a los centros de reciclaje o utiliza los contenedores adecuados.
                    - **Reutiliza envases y materiales:** Usa frascos de vidrio para almacenamiento, cajas de cartón para organizar objetos, y plásticos resistentes para otros usos en el hogar.
                    ### 2. **Compostaje**
                    - **Residuos orgánicos:** Los restos de comida, cáscaras de frutas y verduras, hojas, y otros materiales biodegradables pueden convertirse en compost. El compost es un excelente fertilizante natural para tus plantas.
                    - **Compostera casera:** Si tienes espacio, instala una compostera en tu jardín o en un rincón de tu casa para convertir tus desechos orgánicos en abono.
                    ### 3. **Reutilización Creativa**
                    - **Manualidades y proyectos de bricolaje:** Usa materiales como latas, botellas, y cartón para crear objetos decorativos, juguetes, o útiles domésticos.
                    - **Ropa y textiles:** Transforma ropa vieja en trapos, bolsas reutilizables, o dona lo que esté en buen estado.
                    ### 4. **Reducción del Consumo**
                    - **Compra consciente:** Opta por productos con menos embalaje, elige envases reutilizables, y compra a granel cuando sea posible.
                    - **Evita productos de un solo uso:** Usa bolsas de tela, botellas reutilizables, y otros productos duraderos para reducir la cantidad de residuos que generas.
                    ### 5. **Donaciones**
                    - **Ropa, muebles y electrónicos:** En lugar de tirar artículos que aún funcionan o están en buen estado, dona a organizaciones benéficas, centros de reciclaje de electrónicos, o tiendas de segunda mano.
                    ### 6. **Reciclaje de Residuos Peligrosos*
                    - **Recogida de productos especiales:** Baterías, electrónicos, y productos químicos deben ser llevados a puntos de recogida específicos para ser manejados correctamente y evitar la contaminación.
                    - **Reciclaje de aceite usado:** El aceite de cocina usado puede ser reciclado para hacer biodiesel o llevado a un punto limpio.
                    ### 7. **Trueque e intercambio**
                    - **Intercambia objetos:** Participa en mercados de trueque o grupos de intercambio donde puedas intercambiar cosas que ya no necesitas por otras que sí te sirvan.
                    ### 8. **Eco-bricks**
                    - **Llenado de botellas:** Usa botellas de plástico llenas de residuos plásticos no reciclables para crear eco-ladrillos, que pueden utilizarse en construcción o como material de relleno en proyectos comunitarios.
                    ### 9. **Educación y concienciación**
                    - **Compartir conocimientos:** Enseña a otros en tu comunidad o familia sobre la importancia de reducir, reutilizar, y reciclar. Organiza talleres o charlas para educar sobre cómo aprovechar los residuos.
                    ### 10. **Cocina con aprovechamiento total**
                    - **Aprovechamiento de alimentos:** Usa las cáscaras, huesos, y restos de comida para hacer caldos, abonos o para alimentar animales si es posible.
                    ### Ejemplo de Acción Integral:
                    - **Hacer compost con los restos de comida, reutilizar frascos de vidrio para almacenamiento, y reciclar todos los envases plásticos, metálicos y de papel que se generen en tu hogar. Además, donar la ropa que ya no uses y participar en un intercambio de objetos para darles una segunda vida a tus cosas.**
                    Implementando estas estrategias, no solo reducirás la cantidad de residuos que generas, sino que también estarás contribuyendo a un entorno más sostenible y saludable.{bot.user}!')

@bot.command()
async def errores_al_momento_de_reciclar(ctx):
    await ctx.send(f'Reciclar es una práctica importante, pero a menudo se cometen errores que pueden reducir la efectividad del proceso o incluso contaminar materiales reciclables. Aquí tienes algunos de los errores más comunes al reciclar y cómo evitarlos:
                        ### 1. **No Limpiar los Envases**
                        - **Error:** Colocar envases sucios o con restos de comida en el contenedor de reciclaje.
                        - **Consecuencia:** Los residuos de comida pueden contaminar otros materiales reciclables, haciendo que todo el lote se considere no reciclable.
                        - **Solución:** Enjuaga los envases antes de reciclarlos para asegurarte de que estén limpios.
                        ### 2. **Mezclar Materiales Incorrectamente**
                        - **Error:** Poner materiales no reciclables en el contenedor de reciclaje, como bolsas de plástico, envoltorios de alimentos, o papel encerado.
                        - **Consecuencia:** La mezcla de materiales incorrectos puede dañar las máquinas de reciclaje y contaminar otros materiales reciclables.
                        - **Solución:** Infórmate sobre lo que es reciclable en tu área y sigue las guías locales de reciclaje.
                        ### 3. **No Separar los Materiales Adecuadamente**
                        - **Error:** No separar los diferentes tipos de materiales reciclables, como el papel, el plástico, y el vidrio.
                        - **Consecuencia:** Esto puede dificultar el proceso de reciclaje y reducir la calidad de los materiales reciclados.
                        - **Solución:** Separa los materiales en los contenedores específicos para cada tipo.
                        ### 4. **Reciclar Productos que No Son Reciclables**
                        - **Error:** Reciclar productos como pilas, electrónicos, o textiles a través del sistema de reciclaje doméstico.
                        - **Consecuencia:** Estos materiales requieren un manejo especial y pueden dañar el equipo de reciclaje o ser peligrosos.
                        - **Solución:** Lleva estos materiales a puntos de recogida especializados o centros de reciclaje específicos.
                        ### 5. **Dejar Tapas o Etiquetas en los Envases**
                        - **Error:** Reciclar botellas o frascos con las tapas o etiquetas aún puestas.
                        - **Consecuencia:** Las tapas y etiquetas pueden estar hechas de materiales diferentes que no son reciclables en el mismo proceso.
                        - **Solución:** Retira las tapas y, si es posible, quita las etiquetas antes de reciclar.
                        ### 6. **Reciclar Bolsas de Plástico en el Contenedor de Reciclaje**
                        - **Error:** Colocar bolsas de plástico en el contenedor de reciclaje estándar.
                        - **Consecuencia:** Las bolsas de plástico pueden enredarse en las máquinas de reciclaje, causando paradas en el proceso y daño al equipo.
                        - **Solución:** Lleva las bolsas de plástico a puntos de reciclaje específicos, como los que suelen estar en supermercados.
                        ### 7. **Aplastar Envases de Aluminio**
                        - **Error:** Aplastar latas de aluminio antes de reciclarlas.
                        - **Consecuencia:** Algunas plantas de reciclaje clasifican los materiales por tamaño, y las latas aplastadas pueden ser clasificadas incorrectamente y no recicladas.
                        - **Solución:** Deja las latas de aluminio sin aplastar para asegurar que se clasifiquen correctamente.
                        ### 8. **Reciclar Vidrio Roto**
                        - **Error:** Poner vidrio roto en el contenedor de reciclaje.
                        - **Consecuencia:** El vidrio roto puede ser peligroso para los trabajadores y no siempre es reciclable en los mismos procesos que el vidrio intacto.
                        - **Solución:** Consulta las guías locales, pero en general, el vidrio roto debe ser descartado como basura no reciclable.
                        ### 9. **No Aplanar Cajas de Cartón**
                        - **Error:** Reciclar cajas de cartón sin aplanarlas.
                        - **Consecuencia:** Las cajas no aplanadas ocupan mucho espacio, reduciendo la eficiencia en el transporte y almacenamiento.
                        - **Solución:** Aplana las cajas antes de colocarlas en el contenedor de reciclaje.
                        ### 10. **Desconocer las Normas Locales**
                        - **Error:** No seguir las normas locales de reciclaje.
                        - **Consecuencia:** Diferentes lugares tienen diferentes reglas sobre lo que es reciclable. No seguirlas puede llevar a que los materiales reciclables terminen en el vertedero.
                        - **Solución:** Infórmate sobre las normativas de reciclaje de tu localidad y síguelas al pie de la letra.
                        Evitar estos errores te permitirá reciclar de manera más eficiente y contribuir de manera más efectiva a la sostenibilidad ambiental. {bot.user}!')     

@bot.command()
async def como_ha_afectado_la_contaminacion_ambiental_con_el_desarrolo_del_medio_ambiente_y_porque(ctx):
    await ctx.send(f'La contaminación ambiental ha tenido un impacto significativo y adverso en el desarrollo del medio ambiente por diversas razones. Aquí te explico cómo y por qué:
                    ### 1. **Degradación de Ecosistemas**
                    - **Cómo afecta:** La contaminación del aire, agua y suelo ha provocado la degradación de ecosistemas enteros, afectando la biodiversidad y la capacidad de los entornos naturales para mantener la vida.
                    - **Ejemplo:** Los vertidos de petróleo, pesticidas y otros contaminantes en los cuerpos de agua han destruido hábitats marinos y fluviales, provocando la muerte de muchas especies acuáticas y la desaparición de otras.
                    ### 2. **Pérdida de Biodiversidad**
                    - **Cómo afecta:** La contaminación ha contribuido a la extinción de muchas especies, y amenaza a muchas más, al alterar sus hábitats naturales, contaminarlos con sustancias tóxicas y dificultar su supervivencia.
                    - **Ejemplo:** La contaminación del agua con productos químicos tóxicos ha llevado a la muerte masiva de peces, anfibios y otras especies acuáticas, alterando las cadenas alimenticias y los equilibrios ecológicos.
                    ### 3. **Cambio Climático**
                    - **Cómo afecta:** La emisión de gases de efecto invernadero, como el dióxido de carbono (CO2) y el metano (CH4), ha sido uno de los mayores contribuyentes al calentamiento global y el cambio climático, lo que ha provocado fenómenos climáticos extremos, derretimiento de glaciares, y aumento del nivel del mar.
                    - **Ejemplo:** El aumento de la temperatura global ha afectado a los ecosistemas polares, con el derretimiento de los glaciares y la pérdida de hábitat para especies como el oso polar.
                    ### 4. **Afectación a la Salud Humana y Animal**
                    - **Cómo afecta:** La contaminación del aire y del agua ha llevado a un aumento en enfermedades respiratorias, cardiovasculares y cáncer en humanos, y también afecta a la fauna silvestre que depende de estos recursos.
                    - **Ejemplo:** La contaminación del aire en ciudades altamente industrializadas ha causado un aumento en las tasas de asma, bronquitis crónica, y otras enfermedades respiratorias, tanto en humanos como en animales.
                    ### 5. **Contaminación del Agua**
                    - **Cómo afecta:** La contaminación de ríos, lagos y océanos con productos químicos, plásticos y desechos industriales ha comprometido la calidad del agua, afectando la vida acuática y la disponibilidad de agua potable.
                    - **Ejemplo:** El exceso de nutrientes en cuerpos de agua debido a la escorrentía agrícola ha causado la proliferación de algas tóxicas, lo que lleva a la creación de zonas muertas donde la vida acuática no puede sobrevivir.
                    ### 6. **Acidificación de los Océanos**
                    - **Cómo afecta:** La absorción de CO2 por los océanos ha llevado a su acidificación, afectando la vida marina, especialmente los corales, moluscos y otras especies con conchas de carbonato de calcio.
                    - **Ejemplo:** Los arrecifes de coral están muriendo a un ritmo alarmante debido a la acidificación y el calentamiento de los océanos, lo que afecta a los ecosistemas marinos que dependen de ellos.
                    ### 7. **Desertificación y Degradación del Suelo**
                    - **Cómo afecta:** La contaminación del suelo por productos químicos agrícolas, residuos industriales y desechos urbanos ha llevado a la pérdida de la fertilidad del suelo, contribuyendo a la desertificación y la reducción de la capacidad del suelo para soportar la vida vegetal.
                    - **Ejemplo:** El uso excesivo de pesticidas y fertilizantes ha degradado la calidad del suelo en muchas áreas agrícolas, reduciendo su capacidad para producir cultivos y contribuyendo a la expansión de áreas desérticas.
                    ### 8. **Impacto en el Ciclo del Agua**
                    - **Cómo afecta:** La contaminación y el cambio climático han alterado el ciclo natural del agua, afectando la disponibilidad de agua dulce y alterando los patrones de precipitación.
                    - **Ejemplo:** La deforestación y la contaminación han contribuido a la reducción de la capacidad de los ecosistemas para regular los flujos de agua, causando sequías en algunas áreas e inundaciones en otras.
                    ### **Razones de estos Impactos**
                    - **Crecimiento Industrial:** El rápido crecimiento industrial ha llevado al aumento de la producción de residuos y emisiones, sin una gestión adecuada, lo que ha intensificado la contaminación.
                    - **Expansión Urbana:** La urbanización descontrolada ha aumentado la generación de residuos sólidos y líquidos, que a menudo terminan contaminando el aire, el agua y el suelo.
                    - **Uso de Combustibles Fósiles:** La dependencia de los combustibles fósiles para energía ha sido un gran contribuyente a las emisiones de gases de efecto invernadero y la contaminación del aire.
                    - **Falta de Regulación:** En muchos lugares, la falta de regulaciones ambientales estrictas o la ineficacia en su aplicación ha permitido que las industrias y actividades humanas contaminen sin consecuencias significativas.
                    ### **Conclusión**
                    La contaminación ambiental ha afectado gravemente al desarrollo del medio ambiente al alterar los ecosistemas, reducir la biodiversidad, contribuir al cambio climático, y comprometer la salud de los seres vivos. Estos efectos se deben principalmente a las actividades humanas insostenibles y a la falta de medidas adecuadas para mitigar su impacto. Para proteger y restaurar el medio ambiente, es crucial adoptar prácticas más sostenibles, reducir la contaminación y mejorar la gestión de los recursos naturales. {bot.user}!')        










bot.run("MTI2ODM3Mjg4NjMzNTUyNDg5Ng.Ga-XX7.rpMSLHAW8YYsolFtnLOBMvBmnOQ3rLNQzXrw0U")