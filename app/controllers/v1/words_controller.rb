class V1::WordsController < ApplicationController
  def index
    @words = Word.all

    render json: @words.to_json
  end

  def create
    @word = Word.create(title: params[:title], letter: params[:letter], user: params[:user])

    render json: @word.to_json
  end
end
