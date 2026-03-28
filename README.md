# tennis-stroke-analyzer

A Python-based computer vision tool that analyzes tennis videos and classifies strokes as Topspin, Slice, or Flat.

## Motivation
Improving tennis technique requires understanding your strokes. This tool automates stroke analysis by tracking racket movement and overlaying labels directly on the video.

## How it works
1. Load a tennis video
2. Extract frames
3. Track player pose
4. Classify swing direction
5. Overlay labels on video and gif
6. Export

## Tech Stack
- Python
- OpenCV – video processing
- MediaPipe – pose tracking
- Docker

## Project Status
v1.0 – Prototype complete

Working:
- Pose tracking via MediaPipe
- Track position of relevant body parts
- Stroke classification (Topspin / Slice / Flat)
- Annotated video and GIF export
- Docker setup

Planned for v2.0:
- YOLOv8 racket tracking for improved stroke detection
- Forehand/Backhand/Serve classification 
- Automatic swing segmentation
- Code refactoring and test coverage improvement