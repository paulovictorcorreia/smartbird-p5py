# Smartbird

In this repository, there is the code of a neuroevolution flappybird, which uses genetic algorithm and 
neural networks to make the bird learn how to beat the game. There will be a player script and a genetic algorithm script
to learn to play the game.

![Smart Bird Run](figures/smartbird.gif)


To run the player version, enter the sketches directory and run:


 ` python flappybird.py `

Also, to make bird jump, just press space bar. When the bird dies, click on the screen.

To run the smartbird project, with genetic algorithm to make an AI learn to play the game, run the following command:

` python smartbird.py `

There must be *p5py* installed on your machine and also numpy library.

You can change the difficulty of the game by changing the *framerate* modulos operation on *smartbird.py* and pipe properties on models/Pipe.py.

Finally, this project is based on [Coding Train](https://www.youtube.com/watch?v=c6y21FkaUqw)'s video of neuroevolution algorithm, shoutout to [Daniel Shiffman](https://github.com/CodingTrain) and his amazing job teaching programming!

Obs.: Crossover of genetic algorithm to be implemented yet!
