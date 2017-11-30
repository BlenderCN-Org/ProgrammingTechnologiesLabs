class RacesController < ApplicationController
  before_action :set_race, only: [:show, :update, :destroy]

  # GET /races
  def index
    @races = Race.all
    json_response(@races)
  end

  # POST /races
  def create
    @race = Race.create!(race_params)
    json_response(@race, :created)
  end

  # GET /races/:id
  def show
    json_response(@race)
  end

  # PUT /races/:id
  def update
    @race.update(race_params)
    head :no_content
  end

  # DELETE /races/:id
  def destroy
    @race.destroy
    head :no_content
  end

  private

  def race_params
    # whitelist params
    params.permit(:track, :organization_id, :date)
  end

  def set_todo
    @race = Race.find(params[:id])
  end
end
