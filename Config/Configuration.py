class Configuration:
    # Largeur de la fenêtre du jeu
    WINDOW_WIDTH = 700

    # Hauteur de la fenêtre du jeu
    WINDOW_HEIGHT = 700

    # Taille des blocs sur le plateau de jeu (basée sur la largeur de la fenêtre)
    BLOCK_SIZE = WINDOW_WIDTH // 7

    # Largeur du plateau de jeu (basée sur la largeur de la fenêtre)
    PLATEAU_WIDTH = WINDOW_WIDTH * 7 // 5

    # Hauteur du plateau de jeu (basée sur la hauteur de la fenêtre)
    PLATEAU_HEIGHT = WINDOW_HEIGHT * 7 // 5

    # Nombre de lignes sur le plateau de jeu (basé sur la hauteur de la fenêtre et la taille des blocs)
    LINE_COUNT = WINDOW_HEIGHT // BLOCK_SIZE

    # Nombre de colonnes sur le plateau de jeu (basé sur la largeur de la fenêtre et la taille des blocs)
    COLUMN_COUNT = WINDOW_WIDTH // BLOCK_SIZE
