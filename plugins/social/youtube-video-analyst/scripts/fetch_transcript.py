#!/usr/bin/env python3
"""
YouTube Transcript Fetcher

Extracts transcripts from YouTube videos using the youtube-transcript-api library.
No API key required.

Usage:
    python fetch_transcript.py "https://youtube.com/watch?v=VIDEO_ID"
    python fetch_transcript.py "VIDEO_ID"
    python fetch_transcript.py "https://youtu.be/VIDEO_ID"

Install dependency:
    pip install youtube-transcript-api
"""

import argparse
import re
import sys

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        NoTranscriptFound,
        TranscriptsDisabled,
        VideoUnavailable,
    )
except ImportError:
    print("Error: youtube-transcript-api not installed.")
    print("Install with: pip install youtube-transcript-api")
    sys.exit(1)


def extract_video_id(url_or_id: str) -> str:
    """Extract video ID from various YouTube URL formats or return as-is if already an ID."""

    # Already a video ID (11 characters, alphanumeric with - and _)
    if re.match(r"^[a-zA-Z0-9_-]{11}$", url_or_id):
        return url_or_id

    # Standard YouTube URL: youtube.com/watch?v=VIDEO_ID
    match = re.search(r"[?&]v=([a-zA-Z0-9_-]{11})", url_or_id)
    if match:
        return match.group(1)

    # Short YouTube URL: youtu.be/VIDEO_ID
    match = re.search(r"youtu\.be/([a-zA-Z0-9_-]{11})", url_or_id)
    if match:
        return match.group(1)

    # YouTube Shorts: youtube.com/shorts/VIDEO_ID
    match = re.search(r"shorts/([a-zA-Z0-9_-]{11})", url_or_id)
    if match:
        return match.group(1)

    # Embedded URL: youtube.com/embed/VIDEO_ID
    match = re.search(r"embed/([a-zA-Z0-9_-]{11})", url_or_id)
    if match:
        return match.group(1)

    # If nothing matched, return as-is and let the API handle the error
    return url_or_id


def format_timestamp(seconds: float) -> str:
    """Convert seconds to MM:SS or HH:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def fetch_transcript(video_id: str, include_timestamps: bool = False, language: str = "en") -> str:
    """
    Fetch transcript for a YouTube video.

    Args:
        video_id: YouTube video ID
        include_timestamps: Whether to include timestamps in output
        language: Preferred language code (default: "en")

    Returns:
        Formatted transcript text
    """
    try:
        # Try to get transcript in preferred language first
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        try:
            # Try manual transcript first (usually higher quality)
            transcript = transcript_list.find_manually_created_transcript([language])
        except NoTranscriptFound:
            try:
                # Fall back to auto-generated
                transcript = transcript_list.find_generated_transcript([language])
            except NoTranscriptFound:
                # Fall back to any available transcript
                transcript = transcript_list.find_transcript([language])

        # Fetch the actual transcript data
        transcript_data = transcript.fetch()

        # Format output
        lines = []
        for entry in transcript_data:
            text = entry["text"].strip()
            if not text:
                continue

            if include_timestamps:
                timestamp = format_timestamp(entry["start"])
                lines.append(f"[{timestamp}] {text}")
            else:
                lines.append(text)

        return "\n".join(lines)

    except TranscriptsDisabled:
        return "Error: Transcripts are disabled for this video."
    except VideoUnavailable:
        return "Error: Video is unavailable (private, deleted, or invalid ID)."
    except NoTranscriptFound:
        return f"Error: No transcript found for this video in language '{language}'."
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube video transcripts for analysis.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python fetch_transcript.py "https://youtube.com/watch?v=dQw4w9WgXcQ"
    python fetch_transcript.py "dQw4w9WgXcQ" --timestamps
    python fetch_transcript.py "https://youtu.be/dQw4w9WgXcQ" --lang es
        """
    )
    parser.add_argument(
        "video",
        help="YouTube video URL or video ID"
    )
    parser.add_argument(
        "--timestamps", "-t",
        action="store_true",
        help="Include timestamps in output"
    )
    parser.add_argument(
        "--lang", "-l",
        default="en",
        help="Preferred transcript language (default: en)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: print to stdout)"
    )

    args = parser.parse_args()

    # Extract video ID
    video_id = extract_video_id(args.video)

    # Fetch transcript
    transcript = fetch_transcript(
        video_id,
        include_timestamps=args.timestamps,
        language=args.lang
    )

    # Output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"Transcript saved to: {args.output}")
    else:
        print(transcript)


if __name__ == "__main__":
    main()
