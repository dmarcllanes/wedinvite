from fasthtml.common import *

app, rt = fast_app(hdrs=())

@rt('/styles/style.css')
def get_style(): return FileResponse('styles/style.css')

@rt('/styles/script.js')
def get_script(): return FileResponse('styles/script.js')

@rt('/manifest.json')
def get_manifest():
    return {
        "name": "Sarah & David's Wedding",
        "short_name": "Wedding",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#fdfbf7",
        "theme_color": "#d4af37",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20192%20192'%3E%3Crect%20fill='%23fdfbf7'%20width='192'%20height='192'/%3E%3Ctext%20x='50%25'%20y='50%25'%20font-size='120'%20font-weight='bold'%20fill='%23d4af37'%20text-anchor='middle'%20dy='.3em'%3E%F0%9F%92%95%3C/text%3E%3C/svg%3E",
                "sizes": "192x192",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20512'%3E%3Crect%20fill='%23fdfbf7'%20width='512'%20height='512'/%3E%3Ctext%20x='50%25'%20y='50%25'%20font-size='300'%20font-weight='bold'%20fill='%23d4af37'%20text-anchor='middle'%20dy='.3em'%3E%F0%9F%92%95%3C/text%3E%3C/svg%3E",
                "sizes": "512x512",
                "type": "image/svg+xml",
                "purpose": "maskable"
            }
        ],
        "categories": ["lifestyle"],
        "screenshots": [
            {
                "src": "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%201080'%3E%3Crect%20fill='%23fdfbf7'%20width='540'%20height='1080'/%3E%3Ctext%20x='50%25'%20y='50%25'%20font-size='100'%20font-weight='bold'%20fill='%23d4af37'%20text-anchor='middle'%20dy='.3em'%3EWedding%20Invite%3C/text%3E%3C/svg%3E",
                "sizes": "540x1080",
                "type": "image/svg+xml",
                "form_factor": "narrow"
            }
        ]
    }

@rt('/')
def get():
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Meta(name='description', content='Join us for an unforgettable celebration of love and commitment'),
            Title("Sarah & David's Wedding"),
            Link(href='https://fonts.googleapis.com', rel='preconnect'),
            Link(href='https://fonts.gstatic.com', rel='preconnect', crossorigin=''),
            Link(href='https://fonts.googleapis.com/css2?family=Benne&family=Great+Vibes&family=Montserrat:wght@300;400;600&display=swap', rel='stylesheet'),
            Link(href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css', rel='stylesheet'),
            Link(rel='stylesheet', href='styles/style.css'),
            Meta(name='theme-color', content='#fdfbf7'),
            Meta(name='apple-mobile-web-app-capable', content='yes'),
            Meta(name='apple-mobile-web-app-status-bar-style', content='default'),
            Meta(name='apple-mobile-web-app-title', content='Sarah & David'),
            Link(rel='manifest', href='/manifest.json'),
            Link(rel='icon', type='image/svg+xml', href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 180 180'><rect fill='%23fdfbf7' width='180' height='180'/><text x='50%' y='50%' font-size='100' font-weight='bold' fill='%23d4af37' text-anchor='middle' dy='.3em'>💕</text></svg>"),
            Link(rel='apple-touch-icon', href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 180 180'><rect fill='%23fdfbf7' width='180' height='180'/><text x='50%' y='50%' font-size='100' font-weight='bold' fill='%23d4af37' text-anchor='middle' dy='.3em'>💕</text></svg>")
        ),
        Body(
            Div(
                Div(
                    Span('✨ We are getting married! Join us on June 15, 2026 ✨ '),
                    Span('✨ We are getting married! Join us on June 15, 2026 ✨ '),
                    Span('✨ We are getting married! Join us on June 15, 2026 ✨ '),
                    Span('✨ We are getting married! Join us on June 15, 2026 ✨ '),
                    Span('✨ We are getting married! Join us on June 15, 2026 ✨ '),
                    cls='marquee-content'
                ),
                cls='top-banner'
            ),
            Div(
                Div(
                    Div(
                        P('Install Wedding Invite', style='color: #d4af37; font-weight: 600; margin-bottom: 0.5rem;'),
                        P('Add to your home screen for quick access', style='color: #666; font-size: 0.9rem;')
                    ),
                    Div(
                        Button('Install', id='install-btn', style='background: #d4af37; color: #fff; padding: 0.5rem 1rem; border-radius: 5px; border: none; cursor: pointer; font-weight: 600;'),
                        Button('Close', id='close-install-btn', style='background: transparent; color: #d4af37; border: 1px solid #d4af37; padding: 0.5rem 1rem; border-radius: 5px; cursor: pointer;'),
                        style='display: flex; gap: 0.5rem;'
                    ),
                    style='display: flex; align-items: center; justify-content: space-between; gap: 1rem;'
                ),
                id='install-banner',
                style='display: none; position: fixed; bottom: 20px; left: 20px; right: 20px; z-index: 2000; background: #fff; border: 2px solid #d4af37; border-radius: 10px; padding: 1.5rem; max-width: 400px; margin-left: auto; margin-right: auto; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'
            ),
            
            Div(
                Div(
                    Div(
                        I(cls='fa-solid fa-ring', style='color: var(--gold); font-size: 1.2rem; transform: rotate(-15deg); margin-right: 15px; animation: gentleSway 3s infinite alternate; filter: drop-shadow(0 0 5px rgba(212,175,55,0.5));'),
                        Span('Time until "I Do"', style='font-family: "Great Vibes", cursive; color: var(--gold); font-size: 1.5rem; white-space: nowrap; margin-right: 25px;'),
                        cls='countdown-title-wrapper', style='display: flex; align-items: center;'
                    ),
                    Div(
                        Div(Span('00', id='days', cls='number'), Span('D', cls='label'), cls='mini-unit'),
                        Span(':', style='color: var(--gold); font-weight: bold; margin: 0 5px; animation: pulse 1s infinite alternate;'),
                        Div(Span('00', id='hours', cls='number'), Span('H', cls='label'), cls='mini-unit'),
                        Span(':', style='color: var(--gold); font-weight: bold; margin: 0 5px; animation: pulse 1s infinite alternate; scale: 0.8; transition-delay: 0.2s;'),
                        Div(Span('00', id='minutes', cls='number'), Span('M', cls='label'), cls='mini-unit'),
                        Span(':', style='color: var(--gold); font-weight: bold; margin: 0 5px; animation: pulse 1s infinite alternate; scale: 0.8; transition-delay: 0.4s;'),
                        Div(Span('00', id='seconds', cls='number'), Span('S', cls='label'), cls='mini-unit'),
                        id='timer',
                        cls='countdown-flex'
                    ),
                    cls='countdown-inner',
                    style='display: flex; align-items: center; justify-content: center; width: 100%; max-width: 900px; padding: 0 20px;'
                ),
                id='countdown',
                cls='bottom-sticky-nav'
            ),

            Div(Div(H2('Play background music?', style='margin-bottom: 20px; font-family: "Benne", serif; font-size: 1.8rem;'),
                    Button('Yes', id='modalYes', cls='btn btn-animado', style='margin-right: 15px;'),
                    Button('No', id='modalNo', cls='btn btn-animado'),
                    cls='music-modal-content'), id='musicModal1', cls='music-modal'),
            Header(
                A(I(cls='fa-brands fa-pagelines floral-icon'), ' S&D Wedding', href='#pinicial', cls='logo'),
                Div('☰', cls='menu-toggle', onclick='toggleMenu()'),
                Nav(
                    Ul(
                        Li(A(I(cls='fa-solid fa-ring link-icon'), 'Invitation', href='#pinicial')),
                        Li(A(I(cls='fa-solid fa-ring link-icon'), 'Details', href='#details')),
                        Li(A(I(cls='fa-solid fa-ring link-icon'), 'Itinerary', href='#itinerary')),
                        Li(A(I(cls='fa-solid fa-ring link-icon'), 'RSVP', href='#rsvp')),
                        cls='nav-links'
                    )
                ),
                cls='header'
            ),
            Div(cls='overlay', onclick='toggleMenu()'),
            Nav(Ul(
                Li(A(I(cls='fas fa-envelope'), ' Invitation', href='#pinicial', onclick='toggleMenu()')),
                Li(A(I(cls='fas fa-info-circle'), ' Details', href='#details', onclick='toggleMenu()')),
                Li(A(I(cls='fas fa-list-alt'), ' Itinerary', href='#itinerary', onclick='toggleMenu()')),
                Li(A(I(cls='fas fa-check-circle'), ' RSVP', href='#rsvp', onclick='toggleMenu()')),
            ), id='nav-menu'),

            Main(
                # Section 1: Hero — Interactive 3D Parallax Scene
                Section(
                    # Cursor spotlight (moves with mouse via JS)
                    Div(id='hero-spotlight', cls='hero-spotlight'),

                    # Particles layer (far background — slowest)
                    Div(id='particles-js', cls='particles-overlay hero-parallax-layer', **{'data-depth': '0.1'}),

                    # Ambient orbs (far — slow drift)
                    Div(cls='hero-orb hero-orb-1 hero-parallax-layer', **{'data-depth': '0.15'}),
                    Div(cls='hero-orb hero-orb-2 hero-parallax-layer', **{'data-depth': '0.12'}),

                    # Depth rings layer (mid-back)
                    Div(
                        Div(cls='depth-ring depth-ring-1'),
                        Div(cls='depth-ring depth-ring-2'),
                        Div(cls='depth-ring depth-ring-3'),
                        cls='hero-parallax-layer', **{'data-depth': '0.25'}
                    ),

                    # Floating floral icons (mid — medium speed)
                    Div(
                        I(cls='fas fa-leaf hero-float-icon', style='top:12%; left:8%;'),
                        I(cls='fas fa-heart hero-float-icon', style='top:15%; right:9%; animation-delay: 1.2s;'),
                        I(cls='fas fa-spa hero-float-icon', style='bottom:22%; left:6%; animation-delay: 2.4s;'),
                        I(cls='fas fa-ring hero-float-icon', style='bottom:20%; right:7%; animation-delay: 0.8s;'),
                        I(cls='fas fa-dove hero-float-icon', style='top:38%; left:3%; font-size:1.2rem; animation-delay: 3s;'),
                        I(cls='fas fa-dove hero-float-icon', style='top:35%; right:4%; font-size:1.2rem; animation-delay: 1.8s;'),
                        cls='hero-parallax-layer', **{'data-depth': '0.4'}
                    ),

                    # Glass Monolith — center focal layer
                    Div(
                        Div(
                            # Reveal layer
                            Div(
                                Div(
                                    H2('S & D', cls='reveal-title'),
                                    P("To our dearest family and friends", cls='reveal-text'),
                                    P("We invite you to join us in celebrating our love and new beginnings.", cls='reveal-text'),
                                    Div(A('VIEW DETAILS', href='#details', cls='btn btn-animado', style='margin-top: 1rem;'), cls='open-btn-container'),
                                    cls='reveal-inner'
                                ),
                                cls='monolith-reveal'
                            ),
                            # Left Gate
                            Div(
                                Div(cls='monolith-glare'),
                                Div(H1('S & D', cls='monolith-monogram'), cls='monolith-content'),
                                cls='monolith-gate gate-left'
                            ),
                            # Right Gate
                            Div(
                                Div(cls='monolith-glare'),
                                Div(H1('S & D', cls='monolith-monogram'), cls='monolith-content'),
                                cls='monolith-gate gate-right'
                            ),
                            cls='glass-monolith'
                        ),
                        cls='monolith-container hero-parallax-layer', **{'data-depth': '0.55'}
                    ),


                    id='pinicial', cls='hero-section'
                ),
                
                # SVG Wave Separator
                NotStr('''
                <svg class="wave wave-superior" viewBox="0 0 1440 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                  <path class="wave-base" fill="var(--bg-light)" fill-opacity="1" d="M0,160 C480,240 960,80 1440,160 L1440,320 L0,320 Z"></path>
                </svg>
                '''),
                Section(
                    H1('Details', cls='hidden-element slide-up', style='font-family: "Great Vibes"; font-size: 3.5rem; text-align: center; color: var(--accent); margin-bottom: 3rem;'),
                    Div(
                        # Card 1: Date & Time
                        Div(
                            Div(
                                Div(
                                    I(cls='fas fa-calendar-alt fa-3x', style='color: var(--gold); margin-bottom: 1rem;'),
                                    H3('Date & Time', style='font-family: "Benne", serif; font-size: 1.8rem; color: var(--dark);'),
                                    cls='flip-card-front'
                                ),
                                Div(
                                    P('Saturday, June 15, 2026', style='font-weight: 600; margin-bottom: 0.5rem;'),
                                    P('4:00 PM - Midnight'),
                                    P('Ceremony starts promptly at 4:30 PM.', style='font-size: 0.85rem; margin-top: 1rem; font-style: italic;'),
                                    cls='flip-card-back'
                                ),
                                cls='flip-card-inner'
                            ),
                            cls='flip-card tilt-card scroll-3d hidden-element slide-up'
                        ),
                        # Card 2: Venue
                        Div(
                            Div(
                                Div(
                                    I(cls='fas fa-map-marker-alt fa-3x', style='color: var(--gold); margin-bottom: 1rem;'),
                                    H3('Venue', style='font-family: "Benne", serif; font-size: 1.8rem; color: var(--dark);'),
                                    cls='flip-card-front'
                                ),
                                Div(
                                    H4('The Grand Ballroom', style='font-weight: 600; font-size: 1.2rem; margin-bottom: 0.5rem; color: #fff;'),
                                    P('123 Garden Lane\nCity, State 12345'),
                                    A('GET DIRECTIONS', href='#', target='_blank', cls='btn btn-animado', style='margin-top: 1rem; padding: 0.5rem 1rem; font-size: 0.8rem; display: inline-block; background: transparent; border-color: #fff; color: #fff;'),
                                    cls='flip-card-back'
                                ),
                                cls='flip-card-inner'
                            ),
                            cls='flip-card tilt-card scroll-3d delay-1 hidden-element slide-up'
                        ),
                        # Card 3: Dress Code
                        Div(
                            Div(
                                Div(
                                    I(cls='fas fa-tshirt fa-3x', style='color: var(--gold); margin-bottom: 1rem;'),
                                    H3('Dress Code', style='font-family: "Benne", serif; font-size: 1.8rem; color: var(--dark);'),
                                    cls='flip-card-front'
                                ),
                                Div(
                                    P('Black Tie Optional', style='font-weight: 600; font-size: 1.2rem; margin-bottom: 0.5rem;'),
                                    P('Cocktail Attire Encouraged'),
                                    P('Please avoid wearing white, blush, or the wedding colors (sage green & gold).', style='font-size: 0.85rem; margin-top: 1rem; line-height: 1.4;'),
                                    cls='flip-card-back'
                                ),
                                cls='flip-card-inner'
                            ),
                            cls='flip-card tilt-card scroll-3d delay-2 hidden-element slide-up'
                        ),
                        cls='details-grid'
                    ),
                    id='details', cls='section-padding'
                ),
                Section(
                    H1('Itinerary', cls='hidden-element slide-up', style='font-family: "Great Vibes"; font-size: 3.5rem; text-align: center; color: var(--accent); margin-bottom: 3rem;'),
                    Div(Div(id='progress', cls='progress-line glow-line'),
                        Div(Div(I(cls='fa-regular fa-heart'), cls='circle glow-pulse'), 
                            Div(
                                Div(H3('4:00 P.M.', cls='hidden-element scale-up'), P('Ceremony starts', cls='timeline-desc hidden-element slide-right'), cls='timeline-card'), 
                                cls='text'
                            ), cls='timeline-item left hidden-element slide-right'),
                        Div(Div(I(cls='fa-solid fa-martini-glass-citrus'), cls='circle glow-pulse'), 
                            Div(
                                Div(H3('5:30 P.M.', cls='hidden-element scale-up'), P('Cocktail Hour & Passed Hors d\'oeuvres', cls='timeline-desc hidden-element slide-left'), cls='timeline-card'), 
                                cls='text1'
                            ), cls='timeline-item right hidden-element slide-left'),
                        Div(Div(I(cls='fa-solid fa-utensils'), cls='circle glow-pulse'), 
                            Div(
                                Div(H3('6:30 P.M.', cls='hidden-element scale-up'), P('Grand Reception & Dinner Feast', cls='timeline-desc hidden-element slide-right'), cls='timeline-card'), 
                                cls='text'
                            ), cls='timeline-item left hidden-element slide-right'),
                        Div(Div(I(cls='fa-solid fa-music'), cls='circle glow-pulse'), 
                            Div(
                                Div(H3('8:30 P.M.', cls='hidden-element scale-up'), P('Live Band & DJ Dance Party', cls='timeline-desc hidden-element slide-left'), cls='timeline-card'), 
                                cls='text1'
                            ), cls='timeline-item right hidden-element slide-left'),
                        Div(Div(I(cls='fa-solid fa-car-side'), cls='circle glow-pulse'), 
                            Div(
                                Div(H3('Midnight', cls='hidden-element scale-up'), P('Sparkler Send-off', cls='timeline-desc hidden-element slide-right'), cls='timeline-card'), 
                                cls='text'
                            ), cls='timeline-item left hidden-element slide-right'),
                        cls='timeline'),
                    id='itinerary', cls='section-padding', style='background: var(--bg-light); color: #333;'),
                
                Section(
                    # Falling petals
                    Div(cls='petal', style='left: 10%; width: 15px; height: 15px; animation-duration: 9s, 3s; background: #ffb6b9;'),
                    Div(cls='petal', style='left: 25%; width: 22px; height: 22px; animation-duration: 12s, 4s; animation-delay: 2s, 2s; background: #fae3d9;'),
                    Div(cls='petal', style='left: 45%; width: 12px; height: 12px; animation-duration: 8s, 2.5s; animation-delay: 5s, 5s; background: #bbded6;'),
                    Div(cls='petal', style='left: 65%; width: 18px; height: 18px; animation-duration: 11s, 3.5s; animation-delay: 1s, 1s; background: #ffb6b9;'),
                    Div(cls='petal', style='left: 85%; width: 14px; height: 14px; animation-duration: 10s, 2.8s; animation-delay: 3s, 3s; background: #fae3d9;'),
                    Div(cls='petal', style='left: 5%; width: 16px; height: 16px; animation-duration: 13s, 3.2s; animation-delay: 7s, 7s; background: #bbded6;'),
                    Div(cls='petal', style='left: 75%; width: 20px; height: 20px; animation-duration: 9.5s, 4.2s; animation-delay: 4s, 4s; background: #ffb6b9;'),

                    H1('Our Memories', cls='hidden-element slide-up', style='font-family: "Great Vibes"; font-size: 3.5rem; text-align: center; color: var(--accent); margin-bottom: 3rem; position: relative; z-index: 2;'),
                    
                    Div(
                        Div(
                            # First Set
                            Div(Img(src='https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80', alt='Memory 1', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80', alt='Memory 2', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=600&q=80', alt='Memory 3', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1532712938736-2834cb01b8bf?auto=format&fit=crop&w=600&q=80', alt='Memory 4', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1583939000140-5b5c970428d0?auto=format&fit=crop&w=600&q=80', alt='Memory 5', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1606800052052-a08af7148866?auto=format&fit=crop&w=600&q=80', alt='Memory 6', cls='gallery-img'), cls='gallery-item'),
                            # Duplicated Set for Infinite Loop
                            Div(Img(src='https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80', alt='Memory 1', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80', alt='Memory 2', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=600&q=80', alt='Memory 3', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1532712938736-2834cb01b8bf?auto=format&fit=crop&w=600&q=80', alt='Memory 4', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1583939000140-5b5c970428d0?auto=format&fit=crop&w=600&q=80', alt='Memory 5', cls='gallery-img'), cls='gallery-item'),
                            Div(Img(src='https://images.unsplash.com/photo-1606800052052-a08af7148866?auto=format&fit=crop&w=600&q=80', alt='Memory 6', cls='gallery-img'), cls='gallery-item'),
                            cls='scrolling-track'
                        ),
                        cls='scrolling-wrapper hidden-element slide-up'
                    ),
                    id='memories', cls='section-padding', style='position: relative; overflow: hidden; background: linear-gradient(to bottom, #fff, var(--bg-light)); padding-bottom: 5rem;'
                ),
                Section(
                    Div(
                        # Decorative floating icons
                        I(cls='fas fa-ring bobbing-icon icon-top-left', style='color: var(--gold); position: absolute; top: -20px; left: 10%; font-size: 2.5rem; opacity: 0.8;'),
                        I(cls='fas fa-glass-cheers spinning-icon icon-bottom-right', style='color: var(--gold); position: absolute; bottom: -15px; right: 15%; font-size: 3rem; opacity: 0.8;'),
                        I(cls='fas fa-heart bobbing-icon icon-top-right', style='color: var(--gold); position: absolute; top: 10%; right: 10%; font-size: 1.8rem; opacity: 0.6; animation-delay: 1.5s;'),
                        
                        H1('We would love you to come!', cls='hidden-element slide-up', style='font-family: "Great Vibes"; font-size: clamp(2.5rem, 8vw, 4rem); color: var(--accent); margin-bottom: 2rem; position: relative; z-index: 2;'),
                        P('Kindly secure your reservation and let us celebrate together.', cls='hidden-element slide-up', style='font-family: "Montserrat"; color: var(--dark); margin-bottom: 2rem; position: relative; z-index: 2;'),
                        Button('RSVP NOW', cls='btn btn-animado btn-shimmer hidden-element scale-up', onclick='openAttendanceModal()', style='position: relative; z-index: 2;'), 
                        
                        cls='rsvp-banner tilt-card scroll-3d text-center', style='position: relative; max-width: 800px; margin: 0 auto; padding: 4rem 2rem; border-radius: 20px;'
                    ),
                    Div(Div(Span('×', cls='attendance-close', onclick='closeAttendanceModal()'),
                            H3('Join our Special Day', cls='hidden-element slide-up', style='font-family: "Benne", serif; font-size: 2rem; text-align: center; margin-bottom: 1rem; color: #333;'),
                            P('Please confirm your attendance.', cls='hidden-element slide-up', style='text-align: center; color: #666; margin-bottom: 2rem;'),
                            Form(Div(Label('Full Name *', cls='form-label'), Br(), Input(type='text', id='name', required=True, cls='form-input'), style='margin-bottom: 1.5rem; text-align: left;'),
                                 Div(Label('Will you attend? *', cls='form-label'), Br(),
                                     Select(Option('Yes, I will be there!', value='yes'), Option("Sorry, I can't make it", value='no'), id='attending', required=True, cls='form-input'),
                                     style='margin-bottom: 1.5rem; text-align: left;'),
                                 Div(Label('Dietary restrictions', cls='form-label'), Br(),
                                     Textarea(id='food', placeholder='e.g., Vegan...', cls='form-input', style='height: 80px; resize: vertical;'),
                                     style='margin-bottom: 1.5rem; text-align: left;'),
                                 Button('SEND RSVP', type='submit', cls='btn btn-animado', style='width: 100%; font-size: 1.1rem;'),
                                 id='rsvp-form'),
                            cls='attendance-modal-content'),
                        id='attendanceModal', cls='attendance-modal'),
                    id='rsvp', cls='section-padding')
            ),
            
            # ParticleJS Library
            Script(src='https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js'),
            Audio(Source(src='https://incompetech.com/music/royalty-free/mp3-royaltyfree/Bossa%20Antigua.mp3', type='audio/mp3'), id='audioPlayer', loop=True, preload='auto'),
            Button(I(cls='fa-solid fa-music beat-music'), id='playPauseBtn', cls='music-btn'),
            Script(src='styles/script.js')
        ),
        lang='en'
    )

serve()
