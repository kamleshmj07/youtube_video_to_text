from youtube_transcript_api import YouTubeTranscriptApi as yt


def main():
    #-------------- Enter inputs
    yt_ids = ['CKuAStbkjuA']
    languages = ['en']

    #-------------- Call API
    tuple_trscrpts = yt.get_transcripts(yt_ids, languages=languages)

    #-------------- Process the transcripts
    dict_yt_text = {}
    for id in yt_ids:
        full_text = ''
        list_text_packets = tuple_trscrpts[0][id]

        for pkt in list_text_packets:
            full_text += pkt['text'] + ' '

        dict_yt_text[id] = full_text

    #-------------- Print or log the transcript
    print(dict_yt_text)




#---------------
main()