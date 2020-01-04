* To load the model in Tensorflow-serving, we need to save the model first.
* saved_model
* tf.saved_model.simple_save(keras.backend.get_session(),export_path,
    inputs={'input_image': model.input},
    outputs={t.name:t for t in model.outputs})
 * Use command line utility 'saved_model_cli' 
 * to look at the MetaGraphDefs (the models) |
 * SignatureDefs (the methods you can call) in our SavedModel.
 
 * !saved_model_cli show --dir {export_path} --all
 * Tensorflow serving:
    * add tensorflow-model-server package 
    * Install tensorflow server
    * !apt-get install tensorflow-model-server
    * rest_api_port: The port that you'll use for REST requests.
    * model_name: You'll use this in the URL of REST requests. It can be anything.
    * model_base_path: This is the path to the directory where you've saved your model
    * make json request
    
