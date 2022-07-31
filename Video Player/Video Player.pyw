# Importing useful packages
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys


# Creating Window class for video player
class Window(QWidget):
    # Creating constructor of Window class
    def __init__(self):
        super().__init__()
        # set icon
        self.setWindowIcon(QIcon("A:\\My Projects\\Android Subsystem for Windows (Python)\\Video Player\\video_player_icon.ico"))
        self.setWindowTitle("Video Player")     # set title
        self.setGeometry(100, 50, 1500, 850)        # set geometry

        self.player()       # calling player method

    # defining player method to make video player GUI
    def player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        self.open_button = QPushButton("Open Video")
        self.open_button.clicked.connect(self.open_video)

        self.play_button = QPushButton()
        self.play_button.setEnabled(False)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        h_box = QHBoxLayout()
        h_box.setContentsMargins(0, 0, 0, 0)
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.play_button)
        h_box.addWidget(self.slider)

        v_box = QVBoxLayout()
        v_box.addWidget(videoWidget)
        v_box.addLayout(h_box)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.setLayout(v_box)

        self.mediaPlayer.stateChanged.connect(self.changed_media_state)
        self.mediaPlayer.positionChanged.connect(self.changed_position)
        self.mediaPlayer.durationChanged.connect(self.changed_duration)

    # Creating open_video method to open video
    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.play_button.setEnabled(True)

    # Creating play_video method to play video
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    # Creating changed_media_state method to change media state
    def changed_media_state(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    # Creating changed_position method to change position of slider
    def changed_position(self, position):
        self.slider.setValue(position)

    # Creating changed_duration method to change duration of slider
    def changed_duration(self, duration):
        self.slider.setRange(0, duration)

    # Creating set_position method to set the  position of slider
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


# starting point of program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
