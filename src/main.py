import argparse


from youtube_fetcher import YouTubeFetcher
from sentiment_analyzer import SentimentAnalyzer
from data_calculation import calculate_stats
from display_terminal import show_report


def setup_args():
    parser = argparse.ArgumentParser(description='YouTube Comment Sentiment Analyzer')
    parser.add_argument(
    '--video',        
    dest='video_id',   
    type=str,           
    required=True,      
    help='YouTube video ID (Example ID ---> dQw4w9WgXcQ)'
)
    
    parser.add_argument(
        '--limit', 
        type=int, 
        default=100, 
        help='Maximum number of comments (default: 100)'
    )
    
    return parser.parse_args()


if __name__ == "__main__":
    args = setup_args()
    fetcher = YouTubeFetcher()
    analyzer = SentimentAnalyzer()

    try:
        video_id = args.video_id
        comments = fetcher.fetch_comments(video_id, max_results=args.limit)
        print(f"Comments collected: {len(comments)}")
        analyzer_result = analyzer.analyze_batch(comments)
        result_dict, final_stats = calculate_stats(analyzer_result)
        show_report(result_dict, final_stats)
    except Exception as e:
        print(f"An error occurred: {e}")
