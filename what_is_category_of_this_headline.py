def what_is_category_of_this_headline(headline):
    tokens_of_headline = tokenizer.tokenize(headline)
    max_seq_length = 20
    tokens_of_headline = tokens_of_headline[0:(max_seq_length-2)]
    tokens_of_headline = ['[CLS]',*tokens_of_headline,'[SEP]']
    tokens_of_headline = list(tokens_of_headline)
    if len(tokens_of_headline) < max_seq_length:
        no_of_tokens_remains = max_seq_length - len(tokens_of_headline)
        for i in range(no_of_tokens_remains):
            tokens_of_headline.append("[PAD]")
    padded_token_of_headline = np.array(tokens_of_headline)
    tokens_of_headline = np.array(tokenizer.convert_tokens_to_ids(padded_token_of_headline))
    tokens_of_headline = tokens_of_headline.reshape(1,-1)
    #print(tokens_of_headline)
    
    # Mask Array
    nonzero_elements = np.count_nonzero(list(tokens_of_headline))
    mask_array = [1]*nonzero_elements+[0]*(max_seq_length-nonzero_elements)
    mask_array_of_headline = np.array(mask_array)
    mask_array_of_headline = mask_array_of_headline.reshape(1,-1)
    # segment Array
    segment_array = [0]*max_seq_length
    segment_array_of_headline = np.array(segment_array)
    #print(segment_array_of_headline)
    segment_array_of_headline = segment_array_of_headline.reshape(1,-1)


    #print(tokens_of_headline.shape)
    #print(mask_array_of_headline.shape)
    #print(segment_array_of_headline.shape)

   
    # Giving to Bert
    bert_model_encoded_headline=bert_model.predict([tokens_of_headline, mask_array_of_headline, segment_array_of_headline])
    #print(bert_model_encoded_headline.shape)
    #bert_model_encoded_headline = bert_model_encoded_headline.reshape(-1,1)
    #print(bert_model_encoded_headline.shape)
    
    # Load_model
    model = load_model("/content/drive/MyDrive/1. My_folder/2. AI Projects./3. News_categories_prediction/news_category_predictor.h5")
    
    # Predicting 
    probilities = model.predict(bert_model_encoded_headline)
    #print(probilities)
    label = np.argmax(probilities)
    if label == 0 :
        return """This Headline belongs to 'Health' Category."""
    if label == 1 :
        return """This Headline belongs to 'Business' Category."""
    if label == 2 :
        return """This Headline belongs to 'Entertainment' Category."""
    if label == 3 :
        return """This Headline belongs to 'Science_&_Technology' Category."""
