# tennis-stroke-analyzer 🎾

A Python-based computer vision tool that analyzes tennis videos and classifies strokes as Topspin, Slice, or Flat.

## Motivation
Improving tennis technique requires understanding your strokes. This tool automates stroke analysis by tracking racket movement and overlaying labels directly on the video.

## How it works
1. Load a tennis video
2. Extract frames
3. Track player pose (wrist/elbow) via MediaPipe
4. Classify swing direction → Topspin / Slice / Flat
5. Overlay labels on video and export

## Tech Stack
- Python
- OpenCV – video processing
- MediaPipe – pose tracking
- NumPy – trajectory math
- Docker

## Project Status
- Work in progress