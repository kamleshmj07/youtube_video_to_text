from youtube_transcript_api import YouTubeTranscriptApi as yt

FILES_FOLDER = r'C:\\Users\\kmanjrekar\\Documents\\Linedata\\Personal\\PythonProjects\\youtube_video_to_text\\files\\'


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
        write_text_to_file(FILES_FOLDER + id, full_text)

    # print(dict_yt_text)


def write_text_to_file(fullpath, str_txt):
    '''writing text to file'''
    # Opening a file 
    file_1 = open(fullpath, 'w')
    
    # Writing a string to file 
    file_1.write(str_txt)
        
    # Closing file 
    file_1.close()




#---------------
main()