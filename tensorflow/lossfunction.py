import matplotlib.pyplot as plt
import tensorflow as tf

sess = tf.Session()
x_vals = tf.linspace(-1., 1.0, 500)
target = tf.constant(0.)

# L2 norm is a loss function squaring the difference

l2_y_vals = tf.square(target - x_vals)
l2_y_out = sess.run(l2_y_vals)

l1_y_vals = tf.abs(target - x_vals)
l1_y_out = sess.run(l1_y_vals)

# Pseudo huber loss is a continuous and smooth approximation to the huber loss function.
delta1=0.25
delta2=0.5

phuber1_y_vals = tf.multiply(tf.square(delta1), tf.sqrt(1. + tf.square(target - x_vals)) - 1.)
phuber1_y_out = sess.run(phuber1_y_vals)

phuber2_y_vals = tf.multiply(tf.square(delta2), tf.sqrt(1. + tf.square(target - x_vals)) - 1.)
phuber2_y_out = sess.run(phuber2_y_vals)



x_array = sess.run(x_vals)
plt.plot(x_array, l2_y_out, 'b--',label='L2 Loss')
plt.plot(x_array, l1_y_out, 'r--', label = 'L1 Loss')
plt.plot(x_array, phuber1_y_out, 'k--', label='Huber Loss D=0.25')
plt.plot(x_array, phuber2_y_out, 'g--', label='Huber Loss D=0.5')
plt.legend(loc='lower right', prop={'size': 11})
plt.show()

# For classification function
# Classification loss functions are used to evaluate loss functions when predicting categorical variables

x_vals = tf.linspace(-3., 5., 500)
target = tf.constant(1.)
targets = tf.fill([500,],1.)

# Hinge loss
hinge_y_vals = tf.maximum(0., 1 - tf.multiply(target, x_vals))
hinge_y_out = sess.run(hinge_y_vals)

# Cross entropy loss
xentropy_y_vals = - tf.multiply(target, tf.log(x_vals)) - tf.multiply(1. - target, tf.log(1. - x_vals))
xentropy_y_out = sess.run(xentropy_y_vals)

plt.plot(x_array, hinge_y_out, 'b--', label = 'Hinge Loss')
plt.plot(x_array, xentropy_y_out, 'r--', label = 'Cross Entropy')
plt.show()