var React = require('react')
var ReactDOM = require('react-dom')

var Lead = React.createClass ({
    render: function() {
        return (
            <p>Windowshop and buy the newest items in the market</p>
        )
    }
})

ReactDOM.render(<Lead />, document.getElementById('lead'))