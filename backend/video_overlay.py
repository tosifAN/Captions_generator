import cv2
import textwrap

def add_scrolling_text_overlay(video_file, output_file, full_text, scroll_speed=2):
    cap = cv2.VideoCapture(video_file)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    margin = 50  # Margin from the bottom of the video
    line_height = 30  # Approximate height of each line of text
    max_chars_per_line = frame_width // 18  # Approximate number of characters per line

    # Split the full text into lines that fit within the frame width
    wrapped_text = textwrap.fill(full_text, width=max_chars_per_line)
    text_lines = wrapped_text.split('\n')

    # Initialize the starting position of the text
    y_position = frame_height + margin

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        for i, line in enumerate(text_lines):
            text_y = y_position - i * line_height
            cv2.putText(frame, line, (50, text_y), font, font_scale, (255, 255, 255), font_thickness)

        # Update the vertical position of the text
        y_position -= scroll_speed

        # If the text has scrolled off the screen, reset the position
        if y_position < -len(text_lines) * line_height:
            y_position = frame_height + margin

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
