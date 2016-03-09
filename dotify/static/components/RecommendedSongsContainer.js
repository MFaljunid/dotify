import React from 'react'

import RecommendedSongs from './RecommendedSongs'
import Clear from './Clear'

var RecommendedSongsContainer = React.createClass({
  propTypes: {
    songs: React.PropTypes.array.isRequired,
    handleClearButtonOnClick: React.PropTypes.func.isRequired
  },
  render: function() {
    return (
      <span id="recommended-songs-container">
        <RecommendedSongs songs={this.props.songs} />
        {this.props.songs.length > 0 ? <Clear handleOnClick={this.props.handleClearButtonOnClick} /> : null}
      </span>
    )
  }
})

module.exports = RecommendedSongsContainer;