using System;
using System.Collections.Generic;

// Experimental simple binary classifier using a sigmoid activation 
// based on my limited knowledge of machine learning
// Can only take 2 inputs

//    O
//   / \   
//  O   O + bias

// 1) AddToTrainingSet(): create training set by giving inputs and answers for each example
// 2) Train(): learning rate <= 0.5 and 100 iterations recommended 
// 3) Output(): add new inputs and let it predict answer between 0 and 1


public class Perceptron 
{

    private List<double[]> x = new List<double[]>(); // training inputs
    private List<double> y = new List<double>(); // training answers

    private double b = 1; // not for training! for each new input
    private double[] w = { 0.5, 0.5, 0.5 }; // weights

    // ADD x1 and x2 and y to training set
    public void AddToTrainingSet(double x1, double x2, double yi)
    {
        double[] newSet = new double[3];
        newSet[0] = x1;
        newSet[1] = x2;
        newSet[2] = b;
        x.Add(newSet);
        y.Add(yi);
    }

    private static double Sig(double z)
    {
        return 1.0 / (1.0 + Math.Exp(-z));
    }


    // TRAIN, a = learning rate; iterations = number of times to train 
    public void Train(double a, double iterations) 
    {   
        // how many times to train
        for (int iterate = 0; iterate < iterations; iterate++)
        {   
            //for each training example
            for (int i = 0; i < 3; i++)
            {
                double z = 0;

                //for each input of example 
                for (int j = 0; j < 3; j++)
                {
                    z += (double)x[i][j] * w[j];
                }

                double o = Sig(z);

                //update weights per input after each set
                for (int j = 0; j < 3; j++)
                {
                    w[j] += (double)(a * (y[i] - o) * x[i][j]);
                }
            }

        }
    }

    // RETURN output after training
    public double Output(double x1, double x2)
    {
        double z = x1 * w[0] + x2 * w[1] + b * w[2];
        return (double)Sig(z);
    }




    //END
}


