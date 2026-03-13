
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nuestra Boda | Adam & Valentina</title>

    <!-- Metaetiquetas para SEO y rendimiento -->
    <meta name="description" content="Queremos invitarte a celebrar junto a nosotros este momento único y especial: nuestra boda.">
    <meta name="keywords" content="boda, matrimonio, enlace matrimonial, celebración, amor">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Invitación de Boda | Adam & Valentina">
    <meta property="og:description" content="Queremos invitarte a celebrar junto a nosotros este momento único y especial: nuestra boda.">
    <meta property="og:image" content="https://modern-stationers.github.io/Nuestra-Boda-Adam-y-Valentina/Images/portada.jpeg">
    <meta property="og:url" content="https://modern-stationers.github.io/Nuestra-Boda-Adam-y-Valentina/">

    <!-- Preconexión para recursos externos -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">

    <!-- Preload de imágenes prioritarias -->
    <link rel="preload" href="Elementos/Sobre0.svg" as="image" fetchpriority="high">
    <link rel="preload" href="Elementos/Sobre1.webp" as="image" fetchpriority="high">
    <link rel="preload" href="Elementos/Sobre2.svg" as="image" fetchpriority="high">
    <link rel="preload" href="Elementos/Sello.webp" as="image" fetchpriority="high">
    <link rel="preload" href="Elementos/FlorSeca.png" as="image" fetchpriority="high">

    <!-- Hojas de estilo -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="style.css">

    <!-- Fuentes optimizadas -->
    <link href="https://fonts.googleapis.com/css2?family=Benne&family=Great+Vibes&display=swap" rel="stylesheet">
</head>
<body>

    <!-- Modal de música -->
    <div id="musicModal1" class="music-modal">
      <div class="music-modal-content">
        <h2>¿Deseas escuchar la música de fondo?</h2>
    
        <button id="modalYes" class="btn btn-animado">Sí</button>
        <button id="modalNo" class="btn btn-animado">No</button>
      </div>
    </div>

    <!-- Header Section -->
    <header>
        <div class="menu-toggle" onclick="toggleMenu()">☰</div>
        <h1>Nuestra Boda - Adam & Valentina</h1>
    </header>

    <!-- Overlay for menu -->
    <div class="overlay" onclick="toggleMenu()"></div>

    <!-- Navigation Menu -->
    <nav id="nav-menu">
        <ul>
          <li><a href="#pinicial" onclick="toggleMenu()"><i class="fas fa-home"></i> Inicio</a></li>
          <li><a href="#countdown" onclick="toggleMenu()"><i class="fas fa-hourglass-half"></i> Cuenta regresiva</a></li>
          <li><a href="#gallery" onclick="toggleMenu()"><i class="fas fa-images"></i> Galería</a></li>
          <li><a href="#ceremonia" onclick="toggleMenu()"><i class="fas fa-church"></i> Ceremonia</a></li>
          <li><a href="#recepcion" onclick="toggleMenu()"><i class="fas fa-map-marker-alt"></i> Recepción</a></li>
          <li><a href="#agendar" onclick="toggleMenu()"><i class="far fa-calendar-alt"></i> Fecha</a></li>
          <li><a href="#itinerary" onclick="toggleMenu()"><i class="fas fa-list-alt"></i> Itinerario</a></li>
          <li><a href="#clothes" onclick="toggleMenu()"><i class="fas fa-tshirt"></i> Dress Code</a></li>
          <li><a href="#music-rec" onclick="toggleMenu()"><i class="fas fa-music"></i> Playlist</a></li>
          <li><a href="#gift" onclick="toggleMenu()"><i class="fas fa-gift"></i> Regalo sugerido</a></li>
          <li><a href="#attendance-section" onclick="toggleMenu()"><i class="fas fa-check-circle"></i> Confirmar asistencia</a></li>
        </ul>
    </nav>

    <section id="pinicial">
      <div class="svg-container">
        <!-- Tus SVG (pueden ser inline o con <img src="..."> ) -->
        <div class="wrapper layer1-wrapper">
          <img src="Elementos/Sobre0.svg" alt="Decoración 1" class="svg-layer layer1" loading="eager" fetchpriority="high">
        </div>

        <div class="wrapper audio-wrapper">
          <!-- Botón corazón con play/pause dentro -->
          <button id="playPauseBtn" class="heart-btn">
            <i class="fa-solid fa-heart heart-shape1"></i>
            <i class="fa-solid fa-play play-icon"></i>
          </button>
        
          <!-- Reproductor nativo -->
          <audio id="audioPlayer" loop preload="auto">
            <source src="Music/song.mp3" type="audio/mp3">
            Tu navegador no soporta audio.
          </audio>
        </div>

        <div class="wrapper layer2-wrapper">
          <img src="Elementos/Sobre1.svg" alt="Decoración 2" class="svg-layer layer2" loading="eager" fetchpriority="high">
        </div>
        <div class="wrapper layer3-wrapper">
          <img src="Elementos/Sello.webp" alt="Decoración 3" class="svg-layer layer3" loading="eager" fetchpriority="high">
        </div>
        <img src="Elementos/Sobre2.svg" alt="Decoración 4" class="svg-layer layer4" loading="eager" fetchpriority="high">
        <div class="wrapper layer5-wrapper">
          <img src="Elementos/FlorSeca.png" alt="Decoración 5" class="svg-layer layer5" loading="eager" fetchpriority="high">
        </div>
        <div class="wrapper envelope-wrapper">
          <div class="envelope-container">
            <div class="envelope">
                <div class="flap left"></div>
                <div class="flap right"></div>
                <div class="flap top"></div>
                <div class="flap bottom"></div>
                <div class="seal"></div>
                <div class="click-indicator">
                    <img src="Sobre/mano.png" alt="Toca aquí" class="hand-icon">
                    <span class="click-text">Toca para<br>abrir</span>
                </div>
                <div class="letter">
                    <h4>¡&nbsp;Nos casamos!</h4>

                    <img src="Images/portadap.jpeg" alt="Portada" class="imagen-novios">
            
                    <p class="texto-abajo">Nos encantaría tener el honor de contar con tu valiosa presencia</p>
                </div>
                <div class="stars-container"></div>
            </div>
          </div>
        </div>
        <div class="wrapper layer6-wrapper">
          <img src="Elementos/LogoIniciales.svg" alt="Decoración 6" class="svg-layer layer6" loading="eager" fetchpriority="high">
        </div>
        <div class="wrapper layer7-wrapper">
          <img src="Elementos/FlorSeca.png" alt="Decoración 7" class="svg-layer layer7" loading="eager" fetchpriority="high">
        </div>
    
        <!-- Texto encima -->
        <div class="overlay-text">
          <h2 class="reveal">Adam & Valentina</h2>
          <h3 class="contenedor-texto efecto-zoom">INVITACIÓN ESPECIAL</h3>
          <p id="guestInfo" class="efecto-parrafo zoom-in"></p>
        </div>
      </div>
    </section>

    <!-- Countdown Timer -->
    <section id="countdown">

    <img src="Elementos/ElemCirc.svg" loading="lazy" class="bg-svg">

    <h1 class="reveal">Faltan...</h1>
      <div id="timer">
      <div class="time-unit">
          <span class="number" id="days"></span>
          <span class="label">días</span>
      </div>
      <span class="heart"><i class="fa-solid fa-heart"></i></span>
      <div class="time-unit">
          <span class="number" id="hours"></span>
          <span class="label">horas</span>
      </div>
      <span class="heart"><i class="fa-solid fa-heart"></i></span>
      <div class="time-unit">
          <span class="number" id="minutes"></span>
          <span class="label">min</span>
      </div>
      <span class="heart"><i class="fa-solid fa-heart"></i></span>
      <div class="time-unit">
          <span class="number" id="seconds"></span>
          <span class="label">seg</span>
      </div>
      </div>
    </section>

    <!-- Sección para generar altura -->
    <section id="music">
    </section>

    <!-- Efecto floral -->
    <section id="efecfloral">
      <img src="Elementos/FlorN.svg" id="flor" loading="lazy" class="flor">

      <div class="frases-container">
      <p class="efecto-parrafo zoom-in izquierda">En tu mirada encontré el &nbsp;<span class="otra-letra">camino</span> que siempre busqué.</p>
      <p class="efecto-parrafo zoom-in derecha">En tus manos descubrí la &nbsp;<span class="otra-letra">calma</span> que mi alma soñaba.</p>
      <p class="efecto-parrafo zoom-in izquierda1">Y en nuestro abrazo, la &nbsp;<span class="otra-letra">certeza</span> de un amor que será para siempre.</p>
      </div>

    </section>

    <!-- Photo Gallery -->
    <section id="gallery">

      <div class="clip-wrapper">
        <img src="Elementos/Pin1.webp" alt="Clip" loading="lazy" class="clip-superior">

        <div class="gallery-frame">
          <div class="carousel-container">
            <div class="carousel">
                <div class="carousel-item">
                    <img src="Images/1.png" alt="Photo 3" loading="lazy">
                </div>
            </div>
          </div>
          <p class="efecto-parrafo zoom-in">
            Las imágenes capturan lo que el corazón no puede explicar: la belleza de encontrarnos, de elegirnos y de celebrar el amor que soñamos.</p>
        </div>
      </div>

      

      <div class="clip-wrapper">
         <img src="Elementos/Pin1.webp" alt="Clip" loading="lazy" class="clip-superior1">
         
         <div class="gallery-frame1">
           <div class="carousel-container" data-gallery="2">
            <button class="prev" onclick="moveSlide(-1, 2)">&#10094;</button>
            <div class="carousel">
                <div class="carousel-item"><img src="Images/2.png" alt="Photo 1" loading="lazy"></div>
                <div class="carousel-item"><img src="Images/3.png" alt="Photo 2" loading="lazy"></div>                     
            </div>
            <button class="next" onclick="moveSlide(1, 2)">&#10095;</button>
           </div>
           <div class="carousel-indicators">
            <span class="dot" onclick="setSlide(0,2)"></span>
            <span class="dot" onclick="setSlide(1,2)"></span>
           </div>
        <p class="efecto-parrafo zoom-in">
          Nuestras fotos son más que recuerdos: son la memoria viva de lo que sentimos.</p>
         </div>
      </div>

    </section>
    

    <!-- Event Details -->
    <section id="details">

        <!-- Fondo con SVG -->
        <div class="fondo-svg">
          <img src="Elementos/Detalles.svg" loading="lazy" alt="Decoración" />
        </div>

        <div id="ceremonia">
        <h1 class="reveal">Hora</h1>
        <img src="Video/gif6.gif" alt="GIF de celebración" class="centered-gif" loading="lazy" style="width:80px; height:auto; margin-bottom: -5px;">
        <h3 class="contenedor-texto efecto-zoom">4:00 P.M.</h3>
        </div>

        <div id="recepcion">
        <h2 class="reveal">Lugar</h2>
        <img src="Video/gif1.gif" alt="GIF de celebración" class="centered-gif" loading="lazy" style="width:80px; height:auto; margin-bottom: -5px;">
        <h3 class="contenedor-texto efecto-zoom">Eterna Casa Boutique</h3>
        <p class="adjusted-margin reveal">Vereda el Ciruelar</p>
        <p class="contenedor-texto efecto-fadeSoft">Sopetrán, Antioquia</p>
        <a href="https://maps.app.goo.gl/ecvMontw7wYb3tN87" target="_blank" class="margin btn btn-animado">CÓMO LLEGAR</a>
        </div>

    </section>

    <!-- Agendar evento -->
    <section id="agendar">

          <!-- Fondo con SVG -->
          <div class="fondo-fecha">
            <img src="Elementos/Fecha.svg" loading="lazy" alt="Decoración" />
          </div>

          <div class="texto-fecha">
          <h1 class="contenedor-texto efecto-zoom">Sábado</h1>
          <h2 class="contenedor-texto efecto-zoom">16</h2>
  
          <h3 class="contenedor-texto efecto-deslizar">Mayo</h3>
          <h4 class="contenedor-texto efecto-deslizar">2026</h4>
          <a href="https://calendar.app.google/qR9UFeYaLUr1di4a9" target="_blank" class="ajuste btn1 btn-animado" style="margin-top: 25px">AGENDAR</a>
          </div>
    </section>

    <!-- Itinerary -->
    <section id="itinerary">

        <!-- Fondo con SVG -->
        <div class="fondo-itinerario">
          <img src="Elementos/Itinerario.svg" loading="lazy" alt="Decoración" />
        </div>

        <div class="texto-itinerario">
        <h1 class="reveal">Itinerario</h1>
        <div class="timeline">
          <!-- Línea dorada de progreso -->
          <div class="progress-line" id="progress"></div>
      
          <!-- Item 1 -->
          <div class="timeline-item left">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i></div>
            <div class="text">
            <h3 class="efecto-parrafo zoom-in">4:00 P.M.</h3>
            <p class="efecto-parrafo fade-in">Ceremonia</p>
            </div>
          </div>
      
          <!-- Item 2 -->
          <div class="timeline-item right">
            <div class="text1">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i></div>
            <h3 class="efecto-parrafo zoom-in">4:40 P.M.</h3>
            <p class="efecto-parrafo fade-in">Cóctel de bienvenida</p>
            </div>
          </div>
      
          <!-- Item 3 -->
          <div class="timeline-item left">
            <div class="text">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i></div>
            <h3 class="efecto-parrafo zoom-in">5:30 P.M.</h3>
            <p class="efecto-parrafo fade-in">Ingreso al salón</p>
            </div>
          </div>
      
          <!-- Item 4 -->
          <div class="timeline-item right">
            <div class="text1">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i>
            </div>
            <h3 class="efecto-parrafo zoom-in">5:50 P.M.</h3>
            <p class="efecto-parrafo fade-in">Entrada de los novios</p>
            </div>
          </div>
      
          <!-- Item 5 -->
          <div class="timeline-item left">
            <div class="text">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i></div>
            <h3 class="efecto-parrafo zoom-in">6:10 P.M.</h3>
            <p class="efecto-parrafo fade-in">Sesión de fotos</p>
            </div>
          </div>
          
          <!-- Item 6 -->
          <div class="timeline-item right">
            <div class="text1">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i>
            </div>
            <h3 class="efecto-parrafo zoom-in">6:40 P.M.</h3>
            <p class="efecto-parrafo fade-in">Catering</p>
            </div>
          </div>

          <!-- Item 7 -->
          <div class="timeline-item left">
            <div class="text">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i>
            </div>
            <h3 class="efecto-parrafo zoom-in">8:00 P.M.</h3>
            <p class="efecto-parrafo fade-in">Baile</p>
            </div>
          </div>

          <!-- Item 8 -->
          <div class="timeline-item right">
            <div class="text1">
            <div class="circle"><i class="fa-sharp-duotone fa-regular fa-heart"></i>
            </div>
            <h3 class="efecto-parrafo zoom-in">11:00 P.M.</h3>
            <p class="efecto-parrafo fade-in">Hora loca</p>
            </div>
          </div>

        </div>
        </div>
    </section>

    <!-- OLA SUPERIOR (curvas hacia arriba) -->
    <svg class="wave wave-superior" viewBox="0 0 1440 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
      <!-- Capa base -->
      <path class="wave-base" d="M0,160 C480,240 960,80 1440,160 L1440,320 L0,320 Z"></path>
      <!-- Curva decorativa -->
      <path class="wave-line" d="M0,150 C480,230 960,70 1440,150"></path>
    </svg>

    <!-- Código de vestimenta -->
    <section id="clothes">
        <h1 class="reveal">Código de vestimenta</h1>
        <img src="Video/gif3.gif" alt="GIF de celebración" class="centered-gif" loading="lazy" style="width:170px; height:auto;">
        <p class="contenedor-texto efecto-deslizar">Damas: Vestido largo.<br>Por favor, evita vestir<br>de color blanco.</p>
        <img src="Video/gif2.gif" alt="GIF de celebración" class="centered-gif" loading="lazy" style="width:200px; height:auto; margin-bottom: -25px; margin-top: -25px;">
        <p class="contenedor-texto efecto-deslizar">Caballeros elegantes</p>
        <h3 class="efecto-parrafo slide-right">Ten presente que la zona,<br>por lo general, es de clima<br>cálido y templado.</h3>
        <a href="https://pin.it/4R6AtFraP" target="_blank" class="btn3 btn-animado">SUGERENCIAS</a>
    </section>

    <div class="flor-deco">
      <img src="Elementos/Flor.svg" loading="lazy" alt="Decoración flor">
    </div>

    <!-- Music Recommendation Section -->
    <section id="music-rec">
        <h1 class="reveal">Playlist</h1>
        <img src="Video/gif4.gif" alt="GIF de celebración" class="centered-gif" loading="lazy" style="width:180px; height:auto;">
        <h2 class="contenedor-texto efecto-deslizar">¿Qué canción no puede<br>faltar en la celebración?</h2>
        <p class="efecto-parrafo zoom-in">¡Queremos escuchar tus<br>recomendaciones para que<br>todos disfruten de la música!</p>
        <button class="btn3 btn-animado" onclick="openModal()">SUGERIR MÚSICA</button>
    
        <div id="musicModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal()">&times;</span>
                <h3 class="reveal">Comparte tu canción favorita</h3>
                <form id="musicForm">
                    <input type="text" id="song" placeholder="Nombre de la canción" required>
                    <input type="text" id="artist" placeholder="Intérprete">
                    <input type="url" id="youtube" placeholder="Enlace de YouTube (opcional)">

                    <p id="loadingMessage" style="display: none; margin-top: 20px;color: #000000;">Cargando respuestas...</p>
                    <button type="submit" class="btn1 ajuste1 btn-animado">ENVIAR</button>
                </form>
            </div>
        </div>
    </section>

    <div class="flor-deco2">
      <img src="Elementos/Flor2.svg" loading="lazy" alt="Decoración flor">
    </div>

    <!-- Sección de Confirmación de Asistencia -->
    <section id="attendance-section">
        <h1 class="reveal">¡ Nos encantaría<br>contar contigo!</h1>
        <button class="btn3 btn-animado" onclick="openAttendanceModal()">CONFIRMAR</button>
    
        <div id="attendanceModal" class="attendance-modal">
          <div class="attendance-modal-content">
              <span class="attendance-close" onclick="closeAttendanceModal()">&times;</span>
              <h3 class="reveal">Contamos contigo en nuestro día especial</h3>
              <p class="efecto-parrafo zoom-in">Por favor, confirma tu asistencia para ayudarnos con los preparativos.</p><br>
              <p class="efecto-parrafo zoom-in">Te invitamos a completar este formulario con la información solicitada; tu respuesta será fundamental para organizar cada detalle y asegurarnos de que todos nuestros invitados se sientan cómodos.</p><br>
              
              <div id="attendanceQuestionContainer"></div>
                <form id="attendanceForm">
                  <div id="nameFields" style="display: none;">
                      <label class="form-label" id="guestNamesLabel"></label><br>
                      <textarea id="guestNamesInput"></textarea><br><br>
                  </div>

                  <div id="foodField">
                    <label class="form-label">Restricciones alimentarias o alergias</label><br>
                    <textarea id="foodRestrictionsInput" placeholder="Ej: Sin gluten, alérgico al maní, vegano, etc."></textarea><br><br>
                  </div>
    
                  <div id="messageField">
                      <label class="form-label">Felicitaciones para los novios</label><br>
                      <textarea id="guestMessageInput" placeholder="Escribe tu mensaje aquí..."></textarea><br><br>
                  </div>
                
                  <p id="loadingMessage1" style="display: none;">Cargando respuestas...</p>
                  <button type="submit" class="btn1 btn-animado">ENVIAR</button>
                </form>
              </div>                         
          </div>
      </div>
    </section>

    <section id="ultimo">
    <h1 class="reveal">Te esperamos!</h1>
    </section>

    <!-- JavaScript optimizado -->
    <script src="script.js" defer></script>
    
</body>
</html>
